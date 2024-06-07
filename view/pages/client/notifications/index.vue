<template>
  <div class="h-auto w-full flex flex-col gap-5 p-5">
    <h1 class="text-lg font-semibold text-custom-800 dark:text-white">Notifications</h1>
    <TableNotifications />
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'sidebar'
})

</script>
