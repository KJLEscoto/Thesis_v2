<template>
  <div class="h-auto w-full flex flex-col p-5 gap-5">
    <section class="flex justify-between">
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
      <UButton 
        label="Done" 
        icon="i-lucide-grab" 
        class="dark:text-custom-200 bg-custom-400 hover:bg-custom-500 dark:bg-custom-700 dark:hover:bg-custom-800 rounded p-2" 
        to="/admin/motion-feed"
        size="xs" />
    </section>

    <div class="h-[700px] w-full">
      <Camera />
    </div>
    
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'sidebar'
});

import { user } from '~/assets/js/userSample'

const links = [{
  label: 'Motion Feed',
  to: '/admin/motion-feed'
}, {
  label: 'Train'
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
