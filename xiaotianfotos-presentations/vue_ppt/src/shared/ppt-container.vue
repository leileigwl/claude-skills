<template>
  <div class="ppt-container" @keydown="handleKeyDown" tabindex="0">
    <!-- 幻灯片内容区域 -->
    <div class="slides-viewport">
      <div
        class="slide-wrapper"
        :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
      >
        <div
          v-for="(slide, index) in slides"
          :key="index"
          class="slide"
          :class="{ active: currentSlide === index }"
        >
          <component :is="slide" :isActive="currentSlide === index" />
        </div>
      </div>
    </div>

    <!-- 缩略图面板 -->
    <div class="thumbnails" v-show="showThumbnails">
      <div class="thumbnails-header">
        <h3>{{ thumbnailsLabel }}</h3>
        <button @click="showThumbnails = false">✕</button>
      </div>
      <div class="thumbnails-grid">
        <div
          v-for="(slide, index) in slides"
          :key="index"
          class="thumbnail"
          :class="{ active: currentSlide === index }"
          @click="goToSlide(index)"
        >
          <div class="thumbnail-number">{{ index + 1 }}</div>
          <div class="thumbnail-preview">
            <component :is="slide" :isActive="false" :isPreview="true" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  slides: {
    type: Array,
    required: true
  },
  title: {
    type: String,
    default: 'PPT演示'
  },
  thumbnailsLabel: {
    type: String,
    default: '幻灯片预览'
  }
})

const currentSlide = ref(0)
const showThumbnails = ref(false)
const NAVIGATION_COOLDOWN = 250
let lastNavigationAt = 0

const getTimestamp = () => (typeof performance !== 'undefined' ? performance.now() : Date.now())

const nextSlide = () => {
  const now = getTimestamp()
  if (now - lastNavigationAt < NAVIGATION_COOLDOWN) {
    return
  }
  if (currentSlide.value < props.slides.length - 1) {
    currentSlide.value++
    lastNavigationAt = now
  }
}

const previousSlide = () => {
  const now = getTimestamp()
  if (now - lastNavigationAt < NAVIGATION_COOLDOWN) {
    return
  }
  if (currentSlide.value > 0) {
    currentSlide.value--
    lastNavigationAt = now
  }
}

const goToSlide = (index) => {
  currentSlide.value = index
  showThumbnails.value = false
  lastNavigationAt = getTimestamp()
}

const handleKeyDown = (event) => {
  if (event.repeat) {
    event.preventDefault()
    return
  }
  switch (event.key) {
    case 'ArrowRight':
    case ' ':
      event.preventDefault()
      nextSlide()
      break
    case 'ArrowLeft':
      event.preventDefault()
      previousSlide()
      break
    case 'Home':
      event.preventDefault()
      currentSlide.value = 0
      break
    case 'End':
      event.preventDefault()
      currentSlide.value = props.slides.length - 1
      break
    case 'Escape':
      event.preventDefault()
      showThumbnails.value = !showThumbnails.value
      break
  }
}

onMounted(() => {
  document.title = props.title
  // 自动获取焦点以支持键盘导航
  const container = document.querySelector('.ppt-container')
  if (container) {
    container.focus()
  }
})
</script>

<style scoped>
.ppt-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: radial-gradient(ellipse 80% 60% at 70% 30%, rgba(102, 126, 234, 0.25), transparent 60%),
    radial-gradient(ellipse 70% 50% at 30% 70%, rgba(249, 115, 22, 0.2), transparent 55%),
    radial-gradient(ellipse 60% 40% at 90% 80%, rgba(118, 75, 162, 0.15), transparent 50%),
    #0a0a0a;
  outline: none;
}

.slides-viewport {
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.slide-wrapper {
  display: flex;
  width: 100%;
  height: 100%;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.slide {
  flex: 0 0 100%;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.thumbnails {
  position: fixed;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
  width: 300px;
  max-height: 80vh;
  background: rgba(0, 0, 0, 0.9);
  border-radius: 12px;
  backdrop-filter: blur(20px);
  z-index: 2000;
  overflow: hidden;
}

.thumbnails-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.thumbnails-header h3 {
  color: white;
  margin: 0;
  font-size: 16px;
}

.thumbnails-header button {
  background: none;
  border: none;
  color: white;
  font-size: 18px;
  cursor: pointer;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: background 0.3s ease;
}

.thumbnails-header button:hover {
  background: rgba(255, 255, 255, 0.1);
}

.thumbnails-grid {
  padding: 16px;
  max-height: calc(80vh - 60px);
  overflow-y: auto;
}

.thumbnail {
  width: 100%;
  height: 120px;
  margin-bottom: 12px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.thumbnail:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: scale(1.02);
}

.thumbnail.active {
  background: rgba(102, 126, 234, 0.3);
  border: 2px solid #667eea;
}

.thumbnail-number {
  position: absolute;
  top: 8px;
  left: 8px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  z-index: 10;
}

.thumbnail-preview {
  width: 100%;
  height: 100%;
  transform: scale(0.2);
  transform-origin: top left;
  pointer-events: none;
}

@media (max-width: 768px) {
  .thumbnails {
    width: calc(100vw - 40px);
    right: 20px;
  }
}
</style>
