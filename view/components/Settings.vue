<template>

  <div class="lg:h-screen h-auto w-full p-5 gap-5 flex flex-col justify-between">
    <div class="flex-col gap-5 flex">

      <header class="flex justify-between w-full items-center">
        <h1 class="text-lg font-semibold text-custom-800 dark:text-white">Settings</h1>
        <UButton
          class="bg-red-500 dark:bg-red-500 hover:bg-red-600 dark:hover:bg-red-400 text-white dark:text-white rounded"
          label="Logout" 
          icon="i-lucide-log-out"
          @click="handleLogout" />
      </header>

      <main
        class="flex flex-col h-auto gap-5 p-10 rounded dark:bg-custom-900 bg-custom-100 border border-custom-300 dark:border-custom-700">

        <div class="flex justify-between items-center">
          <h1 class="font-semibold text-lg">Profile</h1>

          <UButton 
            v-if="user.role === 'client'"
            class="flex cursor-pointer justify-center items-center rounded dark:text-white'" 
            label="Edit"
            icon="i-lucide-edit" 
            :to="`/client/settings/${user.username}`" />

          <UButton 
            v-if="user.role === 'admin' || user.role === 'superadmin'"
            class="flex cursor-pointer justify-center items-center rounded dark:text-white'" 
            label="Edit"
            icon="i-lucide-edit" 
            :to="`/admin/settings/${user.username}`" />
        </div>

        <hr class="dark:border-custom-700 border-custom-200">

        <div class="md:flex grid gap-10 h-auto w-full">

          <section
            class="w-52 h-52 rounded-full dark:bg-custom-700 md:mx-10 mx-auto bg-custom-400 flex justify-center items-center cursor-default">
            <span class="font-black text-[150px]">{{ initial }}</span>
          </section>

          <section class="my-auto">
            <div v-for="(p, index) in profile" :key="index" class="grid grid-cols-5 gap-5 my-2">
              <h1 class="capitalize col-span-2">{{ p.label }}: </h1>
              <div class="col-span-2 dark:text-custom-300 text-custom-500 capitalize">
                <UKbd 
                v-if="p.label === 'status'" 
                :class="{
                  'dark:border bg-green-600 dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default px-2': p.value === 'active',
                  'dark:border bg-red-600 dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default px-2': p.value === 'inactive'
                }" 
                :value="p.value" class="col-span-3 text-center mt-2" />

                <div v-else-if="p.label === 'email'">
                  <p class="lowercase">{{ p.value }}</p>
                </div>

                <p v-else> {{ p.value }} </p>
              </div>
            </div>
          </section>

        </div>
      </main>

      <div class="grid md:grid-cols-2 grid-cols-1 h-auto w-full justify-between gap-5">

        <section
          class="h-auto w-full dark:bg-custom-900 bg-custom-100 flex flex-col gap-5 p-10 rounded border border-custom-300 dark:border-custom-700">
          <h1 class="font-semibold text-lg">Login Credentials</h1>
          <hr class="dark:border-custom-700 border-custom-200">
          <section class="my-auto">
            <div 
              v-for="(l, index) in login" 
              :key="index" 
              class="grid grid-cols-3 gap-5 my-2">

              <h1 class="capitalize col-span-1">{{ l.label }}: </h1>
              <p class="col-span-2 dark:text-custom-300 text-custom-500">{{ l.value }}</p>

            </div>
          </section>
        </section>

        <section
          class="h-auto w-full dark:bg-custom-900 bg-custom-100 flex flex-col gap-5 p-10 rounded border border-custom-300 dark:border-custom-700">
          <h1 class="font-semibold text-lg">Timestamps (date & time)</h1>
          <hr class="dark:border-custom-700 border-custom-200">
          <section class="my-auto">
            <div 
              v-for="(t, index) in timestamp" 
              :key="index" 
              class="grid grid-cols-5 gap-5 my-2">

              <h1 class="capitalize col-span-2">{{ t.label }}: </h1>
              <p class="col-span-3 dark:text-custom-300 text-custom-500">{{ t.value }}</p>

            </div>
          </section>
        </section>

      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup lang="ts">

import { user } from '~/assets/js/userLogged';
import { name, playSound } from '~/assets/js/sound'

const initial = computed(() => user.name.charAt(0).toUpperCase());

const profile = [
  {
    label: 'name',
    value: user.name
  },
  {
    label: 'gender',
    value: user.gender
  },
  {
    label: 'phone no.',
    value: user.phone
  },
  {
    label: 'email',
    value: user.email
  },
  {
    label: 'role',
    value: user.role
  },
  {
    label: 'status',
    value: user.status
  },
]

const login = [
  {
    label: 'username',
    value: user.username
  },
  {
    label: 'password',
    value: user.password
  },
]

const timestamp = [
  {
    label: 'account created',
    value: user.account_created
  },
  {
    label: 'last update',
    value: user.updated_at
  },
]

const toast = useToast()
name.value = 'logoff_1'

const handleLogout = () => {
  if (confirm("You would like to log out?") == true) {

  playSound()

  toast.add({
    title: 'Logout Successfully!',
    icon: 'i-lucide-log-out',
    timeout: 2000,
    ui: {
      background : 'dark:bg-orange-700 bg-orange-300', 
      progress: {
        background: 'dark:bg-white bg-orange-700 rounded-full'
      }, 
      ring: 'ring-1 ring-orange-700 dark:ring-custom-900',
      default: {
        closeButton: { 
          color: 'white',
        }
      },
      icon: 'text-custom-900'
    },
  })
  
  navigateTo('/auth')
  } else {
  console.log('Cancelled.')
  }
}
</script>