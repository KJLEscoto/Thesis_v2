<script setup>
const open = ref(false)
</script>

<template>
  <div class="relative">

    <!--mobile-->
    <div class="fixed top-0 left-0 z-30 w-full bg-custom-300 border-custom-500 border-b dark:bg-custom-900">
      <div v-show="!open" class="flex lg:hidden items-center justify-between h-full p-5 tracking-wide">
        <div class="flex gap-3 items-center justify-start">
          <label class="font-semibold text-xl">Client</label>
          <ToggleDarkMode />
        </div>
        <UIcon name="i-lucide-align-justify" class="cursor-pointer left-2 top-2 w-auto h-7 text-custom-600 hover:text-custom-500" @click="open = true"/>
      </div>
      <div v-if="open" class="">
        <ClientSidebarMenu @click="open = false"/>
        <UIcon name="i-lucide-x" class="cursor-pointer right-5 top-5 w-auto h-7 absolute text-red-600 hover:text-red-500" @click="open = false"/>
        <div class="border-t border-t-custom-500">
          <ClientUserItem class="shadow-md" @click="open = false"/>
        </div>
      </div>
    </div>

    <!--desktop-->
    <div class="lg:flex hidden fixed bg-custom-300 border-custom-500 dark:bg-custom-900 h-screen border-r w-auto flex-col justify-between">
      <ClientSidebarMenu />
      <div class="border-t border-custom-500">
        <ClientUserItem /> 
      </div>
    </div>
  </div>
</template>
