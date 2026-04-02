<script setup lang="ts">
defineProps<{ isActive?: boolean; isPreview?: boolean }>()
</script>

<template>
  <section class="slide-shell">
    <h2 class="page-title">AI能做的 vs 你需要做的</h2>
    <div class="cards">
      <div class="card card-left">
        <div class="card-icon">❌</div>
        <h3 class="card-title">AI能做的</h3>
        <div class="card-content">
          <p>帮你生成</p>
          <p>帮你写</p>
          <p>帮你做</p>
        </div>
      </div>
      <div class="card card-right">
        <div class="card-icon">✅</div>
        <h3 class="card-title">你需要做的</h3>
        <div class="card-content">
          <p>盯着把关</p>
          <p>判断对错</p>
          <p>兜底验收</p>
        </div>
      </div>
    </div>
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
  font-size: clamp(1.5rem, 4vw, 2.5rem);
  font-weight: 700;
  color: rgba(255, 255, 255, 0.95);
  margin: 0;
  text-align: center;
}

.cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: clamp(1rem, 3vw, 2rem);
  width: 100%;
  max-width: 900px;
}

.card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1.5rem;
  padding: clamp(1.5rem, 3vw, 2.5rem);
}

.card-right {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.1));
  border-color: rgba(102, 126, 234, 0.3);
}

.card-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.card-title {
  font-size: clamp(1.2rem, 2.5vw, 1.5rem);
  font-weight: 700;
  color: rgba(255, 255, 255, 0.95);
  margin: 0 0 1rem;
}

.card-content p {
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: rgba(255, 255, 255, 0.7);
  margin: 0.5rem 0;
  line-height: 1.6;
}

@media (max-width: 640px) {
  .cards {
    grid-template-columns: 1fr;
  }
}
</style>