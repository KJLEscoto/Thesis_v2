<template>
  <UModal prevent-close :ui="{ background: 'bg-custom-50 dark:bg-custom-900', rounded: 'rounded' }">
    <div class="h-auto w-full p-5 flex flex-col gap-3">

      <section class="flex justify-between items-center">
        <h1 class="text-lg font-semibold">Motion Detected!</h1>
        <!-- <UButton @click="seeNotification" icon="i-lucide-badge-info" trailing label="See Notifications" size="xs" class="rounded"/> -->
        <UIcon name="i-lucide-x" class="text-xl hover:opacity-50 cursor-pointer" @click="closeModal" />
      </section>

      <hr class="border-custom-300 dark:border-custom-700">

      <section class="flex flex-col">
        <div class="flex justify-between items-center">
          <h1 class="font-normal">Name: <span class="font-bold">Walking</span></h1>
          <span class="text-xs text-custom-400">Date captured: --</span>
        </div>
        <p class="text-sm">descriptions/percentage/level --</p>
        <div class="flex justify-center items-center mt-2 w-full bg-white border dark:border-custom-700">
          <img class="w-auto h-[250px]" src="~/assets/img/sample.jpg" alt="img here">
        </div>

      </section>

      <section class="flex justify-between gap-2 w-full">
        <div class="w-full">
          <UButton @click="approveNotification" icon="i-lucide-badge-check" label="Approve"
            class="w-full flex justify-center items-center rounded dark:bg-green-500 dark:hover:opacity-75 dark:hover:bg-green-500 bg-green-500 hover:bg-green-400" />
        </div>
        <div class="w-full">
          <UButton @click="ignoreNotification" icon="i-lucide-badge-minus" label="Ignore"
            class="w-full flex justify-center items-center rounded dark:bg-orange-500 dark:hover:opacity-75 dark:hover:bg-orange-500 bg-orange-500 hover:bg-orange-400" />
        </div>
      </section>

    </div>


  </UModal>
</template>

<script setup>

const modal = useModal()
const toast = useToast()

const closeModal = () => {
  modal.close()
}

const onClick = () => {
  navigateTo('/client/notifications')
  closeModal()
}

const ignoreNotification = () => {
  // status = ignore
  toast.add({
    title: 'Notification Ignored!',
    click: onClick,
    icon: 'i-lucide-badge-minus',
    description: 'Still can be seen in notifications tab.',
    ui: {
      background: 'dark:bg-orange-500 bg-orange-200',
      description: 'text-xs dark:text-custom-100 text-custom-500',
      progress: { background: 'dark:bg-white bg-custom-700 rounded-full' },
      ring: 'ring-1 ring-orange-700 dark:ring-orange-900',
      default: {
        closeButton: { color: 'gray' },
        actionButton: { color: 'red' }
      },
      icon: 'text-custom-900'
    },
  }, closeModal());
}

const approveNotification = () => {
  // status = approve
  toast.add({
    title: 'Notification Approved!',
    click: onClick,
    icon: 'i-lucide-badge-check',
    description: 'See notifications tab for more info.',
    ui: {
      background: 'dark:bg-green-700 bg-green-200',
      description: 'text-xs dark:text-custom-200 text-custom-500',
      progress: { background: 'dark:bg-white bg-custom-700 rounded-full' },
      ring: 'ring-1 ring-green-700 dark:ring-custom-900',
      default: {
        closeButton: { color: 'gray' },
        actionButton: { color: 'red' }
      },
      icon: 'text-custom-900'
    },
  }, closeModal());
}

</script>
