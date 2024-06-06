<template>
  <div class="flex justify-center items-center h-screen w-auto">
    <ToggleDarkMode class="fixed sm:top-20 z-50 top-3 left-3 sm:left-20 duration-200"/>

    <UForm 
      :state="state"
      @submit="onSubmit"
      :validate="validate" 
      @error="onError"
      class="h-auto w-[500px] flex flex-col gap-5 rounded p-8 bg-custom-50 dark:bg-custom-900 shadow-lg border dark:border-custom-700 border-custom-300" >

      <header class="flex items-center justify-center gap-1">
        <UIcon 
          name="i-lucide-shield-check" 
          class="text-3xl" />
        <h1 class="text-2xl font-bold cursor-default">Client Auth</h1>
      </header>

      <hr class="border-custom-300 dark:border-custom-500">

      <!-- username -->
      <UFormGroup 
          class="grid gap-1" 
          name="username" 
          :ui="{error: 'mt-1'}">

          <template #label>
            <div class="flex items-center justify-start gap-1">
              <UIcon 
                name="i-lucide-user-round" 
                class="text-lg" />
              <p class="text-base">Username</p>
            </div>
          </template>

          <template #default="{ error }">
            <UInput 
              v-model="state.username"
              type="text" 
              color="gray" 
              size="md" 
              :trailing-icon="error ? 'i-heroicons-exclamation-triangle-20-solid' : undefined"
              :ui="{
                rounded: 'rounded',
                color: error ? 
                  { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
              }"
              placeholder="Enter username" />
          </template>

            <template #error="{ error }">
              <span :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
              </span>
            </template>
        </UFormGroup>

      <!-- password -->
      <UFormGroup 
          class="grid gap-1"
          name="password"
          :ui="{error: 'mt-1'}">
          <template #label>
            <div class="flex items-center justify-start gap-1">
              <UIcon 
                name="i-lucide-key-round" 
                class="text-lg" />
              <p class="text-base">Password</p>
            </div>
          </template>
          
          <template #default="{ error }">
            <UInput 
              v-model="state.password"
              type="password" 
              color="gray" 
              size="md" 
              :trailing-icon="error ? 'i-heroicons-exclamation-triangle-20-solid' : undefined"
              :ui="{
                rounded: 'rounded',
                color: error ? 
                  { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
              }"
              placeholder="••••••••" />
          </template>

          <template #error="{ error }">
            <span :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
              {{ error ? error : undefined }}
            </span>
          </template>
        </UFormGroup>

      <UButton 
        type="submit"
        :label="label" 
        :loading-icon="loadIcon" 
        :loading="loading" 
        class="flex justify-center items-center gap-1 py-2 rounded dark:text-custom-50" />

      <Divider />

      <UButton 
        to="/login/admin" 
        label="Continue as Admin" 
        icon="i-lucide-square-user-round" 
        class="flex justify-center items-center gap-1 py-2 rounded bg-custom-700 hover:bg-custom-800 dark:bg-custom-600 dark:hover:bg-custom-700 dark:text-custom-50" />

      </UForm>
  </div>
</template>

<script setup lang="ts">

import { user } from '~/assets/js/userSample';
import type { FormError, FormErrorEvent, FormSubmitEvent } from '#ui/types'

const state = reactive({
  username: undefined,
  password: undefined
})

const validate = (state: any): FormError[] => {
  const errors = []
  if (!state.username) errors.push({ path: 'username', message: 'Required' })
  if (!state.password) errors.push({ path: 'password', message: 'Required' })
  return errors
}

const loading = ref(false);
const loadIcon = ref('');
const label = ref('Login');

async function onSubmit (event: FormSubmitEvent<any>) {
  // Do something with data
  console.log(event.data)
  
  loading.value = true;
  loadIcon.value = 'i-lucide-loader-circle';
  label.value = '';

  setTimeout(() => {
    user.role = 'superadmin';
    label.value = 'Login';
    loading.value = false;
    navigateTo('/client/monitor')
  }, 800)
}

async function onError (event: FormErrorEvent) {
  const element = document.getElementById(event.errors[0].id)
  element?.focus()
  element?.scrollIntoView({ behavior: 'smooth', block: 'center' })
}

</script>
