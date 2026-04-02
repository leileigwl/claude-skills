<script setup lang="ts">
defineProps<{ isActive?: boolean; isPreview?: boolean }>()
</script>

<template>
  <section class="slide-shell">
    <div class="quote-block">
      <div class="quote-mark">"</div>
      <p class="quote-text">
        同样的东西，<br />不同人看到的完全不一样。
      </p>
    </div>
  </section>
</template>

<style scoped>
.slide-shell {
  display: flex;
  height: 100%;
  width: 100%;
  align-items: center;
  justify-content: center;
  padding: clamp(2rem, 5vw, 4rem);
}

.quote-block {
  text-align: center;
  max-width: 900px;
}

.quote-mark {
  font-size: clamp(4rem, 10vw, 8rem);
  line-height: 0.5;
  margin-bottom: -2rem;
  background: linear-gradient(135deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  opacity: 0.3;
}

.quote-text {
  font-size: clamp(1.5rem, 4vw, 2.5rem);
  color: rgba(255, 255, 255, 0.85);
  font-style: italic;
  line-height: 1.6;
  margin: 0;
}
</style>