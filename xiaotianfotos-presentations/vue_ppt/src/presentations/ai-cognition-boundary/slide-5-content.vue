<script setup lang="ts">
defineProps<{ isActive?: boolean; isPreview?: boolean }>()
</script>

<template>
  <section class="slide-shell">
    <h2 class="page-title">核心真相</h2>
    <p class="emphasis">AI是你这辈子所有认知的镜像反射</p>
    <ul class="bullets">
      <li class="bullet">
        <div class="diamond"></div>
        <p>你过去学得越多，用AI就越能看见更深的东西</p>
      </li>
      <li class="bullet">
        <div class="diamond"></div>
        <p>没接触过的领域，AI能帮你学得更快——但前提是你得有学习路径</p>
      </li>
      <li class="bullet">
        <div class="diamond"></div>
        <p>你的认知边界，就是AI给你的命运边界</p>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.slide-shell {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  align-items: center;
  justify-content: center;
  padding: clamp(2rem, 5vw, 4rem);
  gap: 1.5rem;
}

.page-title {
  font-size: clamp(1.8rem, 4.5vw, 2.8rem);
  font-weight: 700;
  color: rgba(255, 255, 255, 0.95);
  margin: 0;
}

.emphasis {
  font-size: clamp(1.3rem, 3vw, 1.8rem);
  font-weight: 600;
  background: linear-gradient(135deg, #667eea, #764ba2, #f97316);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin: 0.5rem 0;
  text-align: center;
}

.bullets {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 700px;
  list-style: none;
  padding: 0;
  margin: 0;
}

.bullet {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem 1.25rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 1rem;
}

.diamond {
  width: 10px;
  height: 10px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  transform: rotate(45deg);
  margin-top: 0.5rem;
  flex-shrink: 0;
}

.bullet p {
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: rgba(255, 255, 255, 0.75);
  margin: 0;
  line-height: 1.5;
}
</style>