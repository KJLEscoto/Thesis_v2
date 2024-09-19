<template>
  <UModal prevent-close :ui="{ background: 'bg-custom-50 dark:bg-custom-900', rounded: 'rounded' }">
    <div class="h-auto w-full p-5 flex flex-col gap-3">

      <section class="flex justify-between items-center">
        <h1 class="text-lg font-semibold">Motion Detected</h1>
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

    </div>


  </UModal>
</template>

<script setup>

const modal = useModal()

const closeModal = () => {
  modal.close()
}

</script>
