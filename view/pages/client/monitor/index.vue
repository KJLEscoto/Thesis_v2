<template>
  <div class="lg:h-screen h-[700px] w-full p-5">
    <Camera />
    
    <UButton label="Click me if detected" class="absolute top-52 right-10 rounded" @click="showToast"/>

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
      background : 'dark:bg-red-700 bg-red-300', 
      progress: {background: 'dark:bg-white bg-custom-700 rounded-full'}, 
      ring: 'ring-0', 
      default: {timeout: 2000, actionButton: {color: 'red'}, closeButton: {color: 'cyan'}},
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