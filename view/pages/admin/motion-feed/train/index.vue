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
    </section>
    <section>
      <UForm 
      :state="state"
      @submit="onSubmit"
      :validate="validate" 
      @error="onError"
      class="h-auto w-full flex justify-between gap-5" >
    
      <div class="lg:flex grid gap-5">

      <!-- action -->
      <UFormGroup 
        class="flex items-start gap-2" 
        name="action_name" 
        :ui="{error: 'mt-0'}">

        <template #label>
          <div class="flex items-center justify-start gap-1">
            <p class="text-base">Name:</p>
          </div>
        </template>

        <template #default="{ error }">
          <UInput 
            v-model="state.action_name"
            type="text" 
            class="w-[200px]"
            color="gray" 
            size="xs"
            :ui="{
              rounded: 'rounded',
              color: error ? 
                { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
            }"
            placeholder="action" />
        </template>

          <template #error="{ error }">
            <span :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
              {{ error ? error : undefined }}
            </span>
          </template>
        </UFormGroup>

        <!-- role -->
        <UFormGroup 
          class="flex gap-2"
          name="level" 
          :ui="{error: 'mt-0'}" >
          <template #label>
            <div class="flex items-center justify-start gap-1">
              <p class="text-base">Level:</p>
            </div>
          </template>
          <template #default="{ error }">
            <USelectMenu 
              color="gray" 
              class="w-[200px]"
              selected-icon="i-heroicons-hand-thumb-up-solid"
              size="xs"
              :ui="{
                rounded: 'rounded',
                color: error ? 
                  { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
              }" 
              :uiMenu="{background: 'dark:bg-custom-400', option: {color: 'dark:text-white', active: 'dark:bg-custom-600', empty: 'dark:text-white'}, empty: 'dark:text-white'}" 
              v-model="state.level" 
              :options="levelOptions" 
              placeholder="Select" />
          </template>
          <template #error="{ error }">
            <span :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
              {{ error ? error : undefined }}
            </span>
          </template>
        </UFormGroup>

        <div class="lg:block hidden">
          <UButton 
            label="Done" 
            type="submit"
            icon="i-lucide-grab" 
            class="dark:text-custom-200 bg-custom-400 hover:bg-custom-500 dark:bg-custom-700 dark:hover:bg-custom-800 rounded p-2 flex justify-center" 
            size="xs" />
        </div>
      </div>
      <div class="block lg:hidden">
          <UButton 
            label="Done" 
            type="submit"
            icon="i-lucide-grab" 
            class="dark:text-custom-200 bg-custom-400 hover:bg-custom-500 dark:bg-custom-700 dark:hover:bg-custom-800 rounded p-2 flex justify-center" 
            size="xs" />
        </div>
    </UForm>
    </section>


    <section class="h-[700px] w-full">
      <Camera :isLive="false"/>
    </section>
    
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'sidebar'
});

import { user } from '~/assets/js/userSample'
import type { FormError, FormErrorEvent, FormSubmitEvent } from '#ui/types'

const levelOptions = ['normal', 'warning', 'danger']

const state = reactive({
  action_name: undefined,
  level: undefined
})

const validate = (state: any): FormError[] => {
  const errors = []
  if (!state.action_name) errors.push({ path: 'action_name', message: 'Required' })
  if (!state.level) errors.push({ path: 'level', message: 'Required' })
  return errors
}

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
