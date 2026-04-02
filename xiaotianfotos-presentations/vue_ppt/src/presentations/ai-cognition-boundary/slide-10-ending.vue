<script setup lang="ts">
defineProps<{ isActive?: boolean; isPreview?: boolean }>()
</script>

<template>
  <section class="slide-shell">
    <div class="ending-block">
      <h1 class="headline">学AI，更要追看见能力</h1>
      <p class="subhead">一边用AI，一边把学过的东西变成判断力</p>
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

.ending-block {
  text-align: center;
  max-width: 900px;
}

.headline {
  font-size: clamp(2rem, 6vw, 4rem);
  font-weight: 900;
  letter-spacing: -0.02em;
  margin: 0 0 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f97316 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1.15;
}

.subhead {
  font-size: clamp(1.2rem, 3vw, 1.6rem);
  color: rgba(255, 255, 255, 0.65);
  margin: 0;
  font-weight: 500;
}
</style>