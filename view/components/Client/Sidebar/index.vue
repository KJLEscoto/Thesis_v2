<script setup>
const open = ref(false)
</script>

<template>
  <div class="relative">

    <!--mobile-->
    <section class="fixed top-0 left-0 z-30 w-full bg-custom-500">
      <div v-show="!open" class="flex lg:hidden items-center justify-between h-full p-5 tracking-wide">
        <label class="font-semibold text-xl">Client</label>
        <UIcon name="i-lucide-align-justify" class="cursor-pointer left-2 top-2 w-auto h-7 text-slate-400 hover:text-slate-600" @click="open = true"/>
      </div>
      <div v-if="open">
        <UIcon name="i-lucide-x" class="cursor-pointer right-5 top-5 w-auto h-7 absolute text-red-600 hover:text-red-400" @click="open = false"/>
        <ClientSidebarMenu @click="open = false"/>
      </div>
    </section>

    <!--desktop-->
    <section class="lg:flex hidden lg:fixed bg-custom-300 dark:bg-custom-900 border-custom-500 h-screen border-r w-auto flex-col justify-between">
      <ClientSidebarMenu />
    </section>
  </div>
</template>
