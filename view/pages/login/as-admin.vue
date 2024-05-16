<template>
  <div class="flex justify-center items-center h-screen w-auto">
    <ToggleDarkMode class="fixed lg:top-20 z-50 top-5 left-5 lg:left-20 duration-200"/>
    <div class="h-auto w-1/3 rounded p-10 bg-custom-100 dark:bg-custom-900 shadow-lg">

      <header class="flex items-center justify-between">
        <UButton label="Back" icon="i-lucide-corner-up-left" to="/login/as-client" class="flex justify-center items-center text-sm rounded dark:bg-red-600 dark:hover:bg-red-500 bg-red-700 hover:bg-red-600 dark:text-custom-100" size="2xs"/>
        <div class="flex justify-end items-center gap-1">
          <UIcon name="i-lucide-square-user-round" class="text-3xl"/>
          <h1 class="text-2xl font-bold cursor-default">Admin</h1>
        </div>
      </header>

      <hr class="mt-5 mb-5 border-custom-300">

      <UForm :state="state" class="grid gap-5">

        <section id="username">
          <label class="font-semibold flex gap-1 justify-start items-center">
            <UIcon name="i-lucide-user-round"/>
            <p>Username</p>
          </label>
          <input placeholder="Enter username" type="text"
            class="w-full bg-custom-50 py-2 px-3 rounded border-2 border-custom-200 transition-all duration-300 outline-none focus:border-custom-700 dark:focus:border-custom-50 mt-1"/>
        </section>

        <section id="username">
          <label class="font-semibold flex gap-1 justify-start items-center">
            <UIcon name="i-lucide-key-round"/>
            <p>Password</p>
          </label>
          <input placeholder="Enter password" type="password"
            class="w-full bg-custom-50 py-2 px-3 rounded border-2 border-custom-200 transition-all duration-300 outline-none focus:border-custom-700 dark:focus:border-custom-50 mt-1"/>
        </section>

        <UButton to="/admin/dashboard" label="Login" class="flex justify-center items-center gap-1 py-3 rounded bg-custom-700 hover:bg-custom-800 dark:bg-custom-600 dark:hover:bg-custom-700 dark:text-white"/>

      </UForm>
    </div>
  </div>
</template>

<script setup lang="ts">

const state = reactive({
  email: undefined,
  password: undefined
})

</script>