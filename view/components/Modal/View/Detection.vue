<template>
  <UModal
    :ui="{background: 'bg-custom-50 dark:bg-custom-900', rounded: 'rounded'}" >
    <div class="h-auto w-full p-5 flex flex-col gap-3">

      <section class="flex justify-between">
        <h1 class="text-lg font-semibold">Motion Detected!</h1>
        <UButton @click="seeNotification" icon="i-lucide-badge-info" trailing label="See Notification" size="xs" class="rounded"/>
      </section>

      <hr class="border-custom-300 dark:border-custom-700">

      <section> 
        <div class="flex justify-between items-center">
          <h1 class="font-normal">Title: <span class="font-bold">Snatch</span></h1>
          <span class="text-xs text-custom-400">Date captured: --</span>
        </div>
        <p class="text-sm">descriptions/percentage/level --</p>
      </section>

      <section class="flex justify-between gap-2 w-full">
        <div class="w-full">
          <UButton @click="approveNotification" icon="i-lucide-badge-check" label="Approve" class="w-full flex justify-center items-center rounded dark:bg-green-500 dark:hover:opacity-75 dark:hover:bg-green-500 bg-green-500 hover:bg-green-400"/>
        </div>
        <div class="w-full">
          <UButton @click="closeModal" icon="i-lucide-badge-minus" label="Ignore" class="w-full flex justify-center items-center rounded dark:bg-blue-500 dark:hover:opacity-75 dark:hover:bg-blue-500 bg-blue-500 hover:bg-blue-400"/>
        </div>
      </section>

    </div>

    
  </UModal>
</template>

<script setup>

const modal = useModal()
const toast = useToast()

const closeModal = () => {
  // status = ignore
  modal.close()
}

const seeNotification = () => {
  navigateTo('/client/notifications')
  closeModal()
}

const approveNotification = () => {
  // status = approve
  toast.add({
    title: 'Notification Approved!',
    description: 'See notifications for more info..'
  }, closeModal());
}

</script>


