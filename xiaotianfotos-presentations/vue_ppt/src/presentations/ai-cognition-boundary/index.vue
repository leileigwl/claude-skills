<script setup lang="ts">
import { ref } from 'vue'
import PptContainer from '@/shared/ppt-container.vue'

// 导入所有幻灯片
import Slide1Title from './slide-1-title.vue'
import Slide2Intro from './slide-2-intro.vue'
import Slide3Quote from './slide-3-quote.vue'
import Slide4Split from './slide-4-split.vue'
import Slide5Content from './slide-5-content.vue'
import Slide6Split from './slide-6-split.vue'
import Slide7Metrics from './slide-7-metrics.vue'
import Slide8Split from './slide-8-split.vue'
import Slide9Content from './slide-9-content.vue'
import Slide10Ending from './slide-10-ending.vue'

const slides = [
  Slide1Title,
  Slide2Intro,
  Slide3Quote,
  Slide4Split,
  Slide5Content,
  Slide6Split,
  Slide7Metrics,
  Slide8Split,
  Slide9Content,
  Slide10Ending,
]
</script>

<template>
  <PptContainer :slides="slides" title="AI时代的认知边界" />
</template>