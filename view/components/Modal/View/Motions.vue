<template>
  <UModal 
    prevent-close 
    :ui="{ 
      background: 'bg-custom-50 dark:bg-custom-900', 
      rounded: 'rounded' 
    }">
    <div class="h-auto w-full p-7 flex flex-col gap-3">
      <section class="flex justify-between items-center">
        <h1 class="text-lg font-semibold">Motion Details</h1>
        <UButton icon="i-lucide-x" @click="closeModal"
          class="flex justify-center items-center text-sm rounded-full dark:bg-red-600 dark:hover:bg-red-600/75 bg-red-600 hover:bg-red-600/75 dark:text-custom-100"
          size="2xs" />
      </section>

      <hr class="border-custom-300 dark:border-custom-700">

      <section class="flex flex-col gap-1">
        <div class="flex justify-between items-center">

          <h1 class="font-medium">
            Name: <span class="font-bold capitalize dark:text-custom-300 text-custom-800">{{ selectedMotion.name }}</span>
          </h1>

          <span class="text-xs text-custom-400 font-semibold">
            Date Added: <span class="border-b border-custom-400">{{ selectedMotion.date_added || '--' }}</span>
          </span>
        </div>

        <p class="text-sm font-medium">
          Description: <span class="dark:text-custom-300 text-custom-800 font-normal">{{ selectedMotion.description }}</span>
        </p>

        <p class="text-sm font-medium">Threshold: 
          <span v-if="selectedMotion.threshold <= 74" class="text-green-500 font-extrabold">{{ selectedMotion.threshold }}%</span>
          <span v-else class="text-red-500 font-extrabold">{{ selectedMotion.threshold }}%</span>
        </p>


        <div class="flex justify-center items-center mt-2 w-full bg-white dark:bg-custom-300 border dark:border-custom-700">
          <img 
            v-if="selectedMotion.video_path" 
            class="w-auto h-[300px] object-cover" 
            :src="selectedMotion.video_path" 
            alt="motion video thumbnail">

          <div v-else class="w-auto h-[300px] font-bold text-sm flex justify-center items-center text-red-700">No video available.</div>
        </div>
      </section>
    </div>
  </UModal>
</template>

<script setup>
// Props - receive the selected motion passed from the parent component (Motions.vue)
const props = defineProps({
  selectedMotion: {
    type: Object,
    required: true
  }
});

// Close Modal function
const modal = useModal();
const closeModal = () => {
  modal.close();
};
</script>
