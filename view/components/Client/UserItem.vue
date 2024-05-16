<script setup>
const name = ref('kent escoto')
const usertype = ref('client')

const capitalizedName = computed(() => {
  return name.value.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
});

const initial = name.value.charAt(0).toUpperCase();

</script>

<template>
<!--reveal-->

<div class="m-2 w-auto h-auto">
  <nuxt-link to="#">
    <div class="border rounded-sm border-custom-500 ">
      <UTooltip class="w-full flex justify-start items-center gap-2 relative p-4" :ui="{ background: 'dark:bg-custom-800', arrow: { background: 'dark:before:bg-custom-950'}}" :popper="{ placement: 'bottom' , arrow: true }" text="See Profile">
        <div class="rounded-full bg-custom-400 h-10 w-10 flex justify-center items-center">
          <p class="font-bold text-2xl m-auto">{{ initial }}</p>
        </div>
        <div class="border-l border-custom-400 pl-2">
          <p class="tracking-wide">{{ capitalizedName }}</p>
          <p class="text-custom-500 dark:text-custom-400 font-semibold text-sm tracking-wider">{{ usertype }}</p>
        </div>
        <!-- <UIcon name="i-lucide-chevron-right" class="absolute top-8 right-5 dark:text-custom-500" /> -->
      </UTooltip>
    </div>
  </nuxt-link>
</div>
</template>
