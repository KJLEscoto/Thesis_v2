<template>
  <div class="lg:h-screen h-[700px] w-full p-5">
    <Camera videoUrl="" :isLive="true"/>
    <UButton label="Click me!" class="absolute top-52 right-10 rounded" @click="showToast"/>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'sidebar'
})

import { ModalViewDetection } from '#components'

// for toast
const toast = useToast()
const modal = useModal()

const showToast = () => {
  toast.add({
    title: 'Motion Detected!',
    icon: 'i-lucide-triangle-alert',
    ui: {
      background : 'dark:bg-red-700 bg-red-200', 
      progress: {background: 'dark:bg-white bg-custom-700 rounded-full'}, 
      ring: 'ring-1 ring-red-700 dark:ring-custom-900',
      default: {
        closeButton: { color: 'gray' },
        actionButton: { color: 'red' }
      },
      icon: 'text-custom-900'
    },
    actions: [
      {
        label: 'View',
        click: () => {
          modal.open(ModalViewDetection)
        }
      }
    ],
  });
};
</script>
