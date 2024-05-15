<template>
  <div class="lg:h-screen h-[700px] w-full p-5">
    <div class="border-4 border-custom-500 rounded lg:h-full h-[90%] w-full">
      <div class=" bg-neutral-300 dark:bg-neutral-400 w-full h-full">
        <section v-show="!camera" class="flex items-center justify-center h-full w-full">
          <div class="text-red-800 grid justify-center">
            <UIcon class="w-auto h-10 m-auto" name="i-lucide-video-off" />
              <p class="text-xs tracking-wider font-bold">No Camera Detected.
                <nuxt-link to="/client/settings" class="text-blue-900 underline hover:text-white transition-colors duration-150">Go setup</nuxt-link>
              </p>
          </div>
        </section>
        <section v-show="camera" class="flex items-center justify-center h-full w-full">
            Camera Installed
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'client-sidebar'
})

const camera = ref(false)
</script>