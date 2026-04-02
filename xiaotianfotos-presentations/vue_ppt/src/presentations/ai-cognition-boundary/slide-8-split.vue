<script setup lang="ts">
defineProps<{ isActive?: boolean; isPreview?: boolean }>()
</script>

<template>
  <section class="slide-shell">
    <h2 class="page-title">两个门槛，一降一升</h2>
    <div class="cards">
      <div class="card card-left">
        <div class="card-badge down">↓</div>
        <h3 class="card-title">技术门槛</h3>
        <div class="card-content">
          <p>写代码</p>
          <p>做设计</p>
          <p>剪辑视频</p>
          <p class="hint">AI帮你做</p>
        </div>
      </div>
      <div class="card card-right">
        <div class="card-badge up">↑</div>
        <h3 class="card-title">判断门槛</h3>
        <div class="card-content">
          <p>写得对不对</p>
          <p>设计好不好</p>
          <p>剪辑合不合格</p>
          <p class="hint">你要判断</p>
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
  position: relative;
}

.card-right {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.1));
  border-color: rgba(102, 126, 234, 0.3);
}

.card-badge {
  position: absolute;
  top: -0.75rem;
  right: 1rem;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: 800;
}

.card-badge.down {
  background: linear-gradient(135deg, #22c55e, #16a34a);
  color: white;
}

.card-badge.up {
  background: linear-gradient(135deg, #f97316, #ea580c);
  color: white;
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
  margin: 0.4rem 0;
  line-height: 1.5;
}

.card-content .hint {
  margin-top: 0.8rem;
  color: rgba(255, 255, 255, 0.5);
  font-size: clamp(0.9rem, 1.8vw, 1rem);
}

@media (max-width: 640px) {
  .cards {
    grid-template-columns: 1fr;
  }
}
</style>