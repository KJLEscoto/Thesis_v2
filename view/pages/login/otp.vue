<template>
  <div class="flex justify-center items-center h-screen w-auto">
    <ToggleDarkMode class="fixed sm:top-20 z-50 top-3 left-3 sm:left-20 duration-200" />

    <UForm :state="state" @submit="onSubmit" :validate="validate" @error="onError"
      class="h-auto w-[500px] flex flex-col gap-5 rounded p-8 bg-custom-50 dark:bg-custom-900 shadow-lg border dark:border-custom-700 border-custom-300">

      <header class="flex items-center justify-between gap-1">
        <div class="flex justify-end items-center gap-1">
          <UIcon name="i-lucide-message-square-more" class="text-3xl" />
          <h1 class="text-2xl font-bold cursor-default">OTP Verification</h1>
        </div>
        <UButton label="Cancel" icon="i-lucide-x" @click="goBack"
          class="flex justify-center items-center text-sm rounded dark:bg-red-600 dark:hover:bg-red-500 bg-red-700 hover:bg-red-600 dark:text-custom-100"
          size="2xs" />
      </header>

      <hr class="border-custom-300 dark:border-custom-500">

      <!-- otp -->
      <UFormGroup class="flex flex-col gap-1" name="otp" :ui="{ error: 'mt-1', label: '' }">

        <template #label>
          <div class="flex flex-col justify-center font-bold mb-2 items-center w-full">
            <p class="font-normal">Enter the code from the SMS we sent to</p>
            <p>{{ user.phone }}</p>
          </div>
        </template>

        <template #default="{ error }">
          <UInput v-model="state.otp" type="text" color="gray" size="md"
            :trailing-icon="error ? 'i-heroicons-exclamation-triangle-20-solid' : undefined" :ui="{
              rounded: 'rounded',
              color: error ?
                { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
            }" placeholder="Enter 6 digit pin" />
        </template>

        <template #error="{ error }">
          <span
            :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
            {{ error ? error : undefined }}
          </span>
        </template>
      </UFormGroup>

      <UButton type="submit" :label="label" :loading-icon="loadIcon" :loading="loading"
        class="flex justify-center items-center gap-1 py-2 rounded dark:text-custom-50" />

      <p class="text-xs">type lang sa bisan unsa para maka submit</p>

    </UForm>
  </div>
</template>

<script setup lang="ts">

import { user } from '~/assets/js/userSample';
import type { FormError, FormErrorEvent, FormSubmitEvent } from '#ui/types'

const state = reactive({
  otp: undefined
})

const validate = (state: any): FormError[] => {
  const errors = []
  if (!state.otp) errors.push({ path: 'otp', message: 'Required' })
  return errors
}

const loading = ref(false);
const loadIcon = ref('');
const label = ref('Submit');

async function onSubmit(event: FormSubmitEvent<any>) {
  // Do something with data
  console.log(event.data)

  loading.value = true;
  loadIcon.value = 'i-lucide-loader-circle';
  label.value = '';

  setTimeout(() => {
    // yawa nag bug ni? ang role kay client pero superadmin ang ma console.. pa fix nlng po (update: need i refresh ang page haha bago mag submit)
    console.log(user.role);

    // Conditional navigation based on user role
    if (user.role === 'client') {
      navigateTo('/client/monitor');
    } else if (user.role === 'admin' || user.role === 'superadmin') {
      navigateTo('/admin/dashboard');
    } else {
      navigateTo('#');
    }

    label.value = 'Submit';
    loading.value = false;
  }, 800);
}

async function onError(event: FormErrorEvent) {
  const element = document.getElementById(event.errors[0].id)
  element?.focus()
  element?.scrollIntoView({ behavior: 'smooth', block: 'center' })
}

const router = useRouter();

const goBack = () => {
  router.go(-1);
};
</script>
