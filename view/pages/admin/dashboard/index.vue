<template>

  <UseHead title="Dashboard - Admin"/>

  <div class="h-auto w-full p-5 flex flex-col gap-5">
    <h1 class="text-lg font-semibold text-custom-800 dark:text-white">Dashboard</h1>

    <div class="grid grid-cols-2 gap-5 w-full h-auto">
      <section class="flex flex-col gap-5">
        <h1>Recently Detected</h1>

        <UCarousel
          ref="carouselRef"
          v-slot="{ item }"
          :items="items"
          :ui="{ item: 'basis-full' }"
          class="overflow-hidden w-auto"
          indicators >

          <img :src="item" class="w-full" draggable="false">

        </UCarousel>
      </section>

      <section class="flex flex-col gap-5">
        <h1 class="">List of Motions</h1>

        <div class="h-full bg-slate-500">

        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'sidebar'
})

// fetch screenshots
const items = [
  'https://picsum.photos/1920/1080?random=2',
  'https://picsum.photos/1920/1080?random=3',
  'https://picsum.photos/1920/1080?random=1',
  'https://picsum.photos/1920/1080?random=4',
  'https://picsum.photos/1920/1080?random=5',
  'https://picsum.photos/1920/1080?random=6'
]

const carouselRef = ref()

onMounted(() => {
  setInterval(() => {
    if (!carouselRef.value) return

    if (carouselRef.value.page === carouselRef.value.pages) {
      return carouselRef.value.select(0)
    }

    carouselRef.value.next()
  }, 3000)
})

</script>