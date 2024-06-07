<template>
  <div class="h-auto w-full flex flex-col p-5 gap-10">
    <section class="">
      <UBreadcrumb :links="links">    
        <template #divider>
          <UIcon 
            name="i-lucide-chevron-right" 
            class="text-lg" />
        </template>
        <template #default="{ link, isActive }">
          <div 
            :class="{'dark:text-white text-custom-800 text-lg cursor-default': isActive, 
            'text-custom-300 hover:text-custom-500 hover:dark:text-custom-300 dark:text-custom-500 text-lg': !isActive}" 
            class="rounded-full" >
            {{ link.label }}
          </div>
        </template>
      </UBreadcrumb>
    </section>
    <section class="h-4/5 w-full flex justify-center items-center">
      <div class="sm:w-3/4 w-full h-auto flex flex-col gap-5">
        <div class="flex justify-between">
                
          <div class="font-semibold cursor-default flex items-center gap-1 w-1/2">
            <UIcon 
              name="i-lucide-book-user" 
              class="text-xl" />
            <h1 class="font-bold text-xl">User Details</h1>
          </div>
          
          <div class="flex justify-end w-1/2 gap-x-2">
            <section class="w-auto">
              <UButton 
                label="Back" 
                icon="i-lucide-move-left"
                class="flex justify-center w-full items-center rounded dark:bg-red-600 dark:hover:bg-red-500 bg-red-700 hover:bg-red-600 dark:text-custom-100" 
                to="/admin/users" />
            </section>
            <section class="w-auto">
              <UTooltip text="Only superadmin can edit" v-if="user.role === 'admin'">
                <UButton 
                  :disabled="user.role === 'admin'"
                  :class="user.role === 'admin' ? 'opacity-20 cursor-not-allowed' : 'flex cursor-pointer justify-center w-full items-center rounded dark:text-white'"
                  label="Edit"
                  icon="i-lucide-edit"
                  to="/admin/users/read/update/1" />
              </UTooltip>
            </section>
          </div>
        </div>

          
          <p>-- retrieve ang info sa user gamit iyang ID -- </p>

        <div class="lg:flex grid gap-5 w-full">
          <section class="bg-custom-100 dark:bg-custom-900 border border-custom-300 dark:border-custom-700 rounded p-5 lg:w-1/2 w-full">
            <h1 class=" font-semibold">Personal Information</h1>
            <hr class="border-custom-200 dark:border-custom-700 mt-2 mb-2">
            <section class="my-auto">
              <div v-for="(p, index) in profile" :key="index" class="grid grid-cols-3 gap-5 my-2">
                <h1 class="capitalize col-span-1">{{ p.label }}: </h1>
                <div class="col-span-2 dark:text-custom-300 text-custom-500 capitalize">
                    <UKbd 
                    v-if="p.label === 'status'"
                    :class="{
                      'dark:border bg-green-600 dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default': p.value === 'active',
                      'dark:border bg-red-600 dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default': p.value === 'inactive'
                    }" 
                    :value="p.value" 
                    class="col-span-3 text-center mt-2"
                  />
                  <p v-else> {{ p.value }} </p>
                </div>
                
              </div>
            </section>
          </section>
          <div class="flex flex-col gap-5 lg:w-1/2 w-full">
            <section class="bg-custom-100 dark:bg-custom-900 rounded p-5 border border-custom-300 dark:border-custom-700">
              <h1 class=" font-semibold">Login Credentials</h1>
              <hr class="border-custom-200 dark:border-custom-700 mt-2 mb-2">
              <section class="my-auto">
                <div v-for="(l, index) in login" :key="index" class="grid grid-cols-3 gap-5 my-2">
                  <h1 class="capitalize col-span-1">{{ l.label }}: </h1>
                  <p class="col-span-2 dark:text-custom-300 text-custom-500">{{ l.value }}</p>
                </div>
              </section>
            </section>
            <section class="bg-custom-100 dark:bg-custom-900 rounded p-5 border border-custom-300 dark:border-custom-700">
              <h1 class=" font-semibold">Timestamps (date & time)</h1>
              <hr class="border-custom-200 dark:border-custom-700 mt-2 mb-2">
              <section class="my-auto">
                <div v-for="(t, index) in timestamp" :key="index" class="grid grid-cols-5 gap-5 my-2">
                  <h1 class="capitalize col-span-2">{{ t.label }}: </h1>
                  <p class="col-span-3 dark:text-custom-300 text-custom-500 capitalize">{{ t.value }}</p>
                </div>
              </section>
            </section>
          </div>
        </div>
      </div>
    </section>
    <hr class="border-custom-300 dark:border-custom-800">
    <section class="sm:w-3/4 w-full mx-auto flex flex-col gap-5">
      <div class="font-semibold cursor-default flex items-center gap-1 w-1/2">
        <UIcon 
          name="i-lucide-book-open-text" 
          class="text-xl" />
        <h1 class="font-bold text-xl">Notifications Log</h1>
      </div>
      <p>-- retrieve ang notifications sa user --</p>
      <TableNotifications />
    </section>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'sidebar'
});

import { user } from '~/assets/js/userSample'

const links = [{
  label: 'Users',
  to: '/admin/users'
}, {
  label: 'Read'
}];

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


</script>
