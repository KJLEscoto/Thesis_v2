<template>
  <div class="h-screen w-full p-5 flex flex-col justify-between">
    <div class="flex-col gap-5 flex">
      <header class="flex justify-between w-full items-center">
        <h1 class="text-lg font-semibold text-custom-800 dark:text-white">Settings</h1>
        <UButton 
          class="bg-red-500 dark:bg-red-500 hover:bg-red-600 dark:hover:bg-red-400 text-white dark:text-white rounded" 
          label="Logout" 
          icon="i-lucide-log-out"/>
      </header>
      <main class="flex flex-col h-auto gap-5 p-5 rounded dark:bg-custom-900 bg-custom-100">
        <h1 class="font-semibold text-lg">Profile</h1>
        <hr class="dark:border-custom-700 border-custom-200">
        <div class="flex gap-10 h-auto w-full">
          <section class="w-52 h-52 rounded-full dark:bg-custom-700 bg-custom-400 flex justify-center items-center cursor-default">
            <span class="font-black text-[150px]">{{ initial }}</span>
          </section>
          <section class="grid grid-cols-2 gap-2">
            <h1>Name:</h1>
            <p class="capitalize">{{ user.name }}</p>
            <h1>Gender:</h1>
            <p class="capitalize">{{ user.gender }}</p>
            <h1>Phone:</h1>
            <p>{{ user.phone }}</p>
            <h1>Role:</h1>
            <p>{{ user.role }}</p>
            <h1>Status:</h1>
            <p>{{ user.status }}</p>
          </section>
        </div>
      </main>
      <div class="flex h-auto w-full justify-between gap-5">
        <section class="h-auto w-full dark:bg-custom-900 bg-custom-100 flex flex-col gap-5 p-5 rounded">
          <h1 class="font-semibold text-lg">Login Credentials</h1>
          <hr class="dark:border-custom-700 border-custom-200">
          <section class="grid grid-cols-2 gap-2">
            <h1>Username:</h1>
            <p>{{ user.username }}</p>
            <h1>Password:</h1>
            <p>{{ user.password }}</p>
          </section>
        </section>
        <section class="h-auto w-full dark:bg-custom-900 bg-custom-100 flex flex-col gap-5 p-5 rounded">
          <h1 class="font-semibold text-lg">Timestamps (date & time)</h1>
          <hr class="dark:border-custom-700 border-custom-200">
          <section class="grid grid-cols-2 gap-2">
            <h1>Account Created:</h1>
            <p>{{ user.account_created }}</p>
            <h1>Last Update:</h1>
            <p>{{ user.updated_at }}</p>
          </section>
        </section>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup>

import { user } from '~/assets/js/userSample';

const initial = computed(() => user.name.charAt(0).toUpperCase());

definePageMeta({
  layout: 'sidebar'
})

</script>