<template>
  <div class="h-auto w-full p-5 flex flex-col gap-5">
    <div class="flex justify-between items-center">
      <h1 class="text-lg font-semibold text-custom-800 dark:text-white">Motion Feed</h1>
      <div class="lg:hidden block">
        <UButton 
          label="Go Train" 
          icon="i-lucide-hand" 
          class="dark:text-custom-200 bg-custom-400 hover:bg-custom-500 dark:bg-custom-700 dark:hover:bg-custom-800 rounded p-2" 
          to="/admin/motion-feed/train"
          size="xs" />
      </div>
    </div>
    <TableTrainings />
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'sidebar'
})

</script>