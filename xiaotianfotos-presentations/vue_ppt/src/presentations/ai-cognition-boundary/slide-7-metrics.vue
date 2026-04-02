<script setup lang="ts">
defineProps<{ isActive?: boolean; isPreview?: boolean }>()
</script>

<template>
  <section class="slide-shell">
    <h2 class="page-title">差距在哪？看见能力</h2>
    <div class="metrics">
      <div class="metric-card">
        <div class="metric-value">认知</div>
        <div class="metric-label">真正的资产</div>
      </div>
      <div class="metric-card">
        <div class="metric-value">经验</div>
        <div class="metric-label">评审标准</div>
      </div>
      <div class="metric-card">
        <div class="metric-value">判断思路</div>
        <div class="metric-label">可复用的框架</div>
      </div>
    </div>
    <p class="summary">别人只能生成，你能判断、能修正、能验收</p>
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
  gap: 2rem;
}

.page-title {
  font-size: clamp(1.8rem, 4.5vw, 2.8rem);
  font-weight: 700;
  color: rgba(255, 255, 255, 0.95);
  margin: 0;
}

.metrics {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: clamp(1rem, 2vw, 1.5rem);
  width: 100%;
  max-width: 900px;
}

.metric-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1.25rem;
  padding: clamp(1.25rem, 2.5vw, 2rem);
  text-align: center;
}

.metric-value {
  font-size: clamp(1.8rem, 4vw, 2.5rem);
  font-weight: 800;
  background: linear-gradient(135deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.5rem;
}

.metric-label {
  font-size: clamp(0.9rem, 1.5vw, 1.1rem);
  color: rgba(255, 255, 255, 0.6);
}

.summary {
  font-size: clamp(1rem, 2vw, 1.25rem);
  color: rgba(255, 255, 255, 0.7);
  margin: 0;
  text-align: center;
}

@media (max-width: 640px) {
  .metrics {
    grid-template-columns: 1fr;
  }
}
</style>