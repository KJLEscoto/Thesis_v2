<template>

  <UseHead title="SMS - Auth" description="SMS - phone number verification." />

  <div class="flex justify-center items-center h-screen w-auto">

    <ToggleDarkMode class="fixed sm:top-20 z-50 top-3 left-3 sm:left-20 duration-200" />

    <UForm 
      :state="state" 
      @submit="onSubmit" 
      :validate="validate" 
      @error="onError"
      class="h-auto w-[500px] flex flex-col gap-4 rounded p-8 bg-custom-50 dark:bg-custom-900 shadow-lg border dark:border-custom-700 border-custom-300">

      <header>
        <div class="flex items-center justify-end">
          <UButton icon="i-lucide-x" @click="goBack"
              class="flex justify-center items-center text-sm rounded-full dark:bg-red-600 dark:hover:bg-red-600/75 bg-red-600 hover:bg-red-600/75 dark:text-custom-100"
              size="2xs" />
        </div>
        <div class="flex justify-center items-center gap-1">
          <UIcon 
            name="i-lucide-message-square-more" 
            class="text-3xl" />
          <h1 class="text-2xl font-bold cursor-default">SMS Verification</h1>
        </div>
      </header>

      <hr class="border-custom-300 dark:border-custom-500">

      <!-- otp -->
      <UFormGroup 
        class="flex flex-col gap-1" 
        name="otp" 
        :ui="{ error: 'mt-1', label: '' }">

        <template #label>
          <div class="flex flex-col justify-center mb-2 items-center w-full">
            <p class="font-normal">Enter the code from the <strong>SMS</strong> we sent to</p>
            <p class="font-medium text-base italic text-blue-700 dark:text-blue-500">{{ user.phone }}</p>
          </div>
        </template>

        <template #default="{ error }">
          <UInput 
            v-model="state.otp" 
            placeholder="6-digit pin"
            type="text" 
            color="gray" 
            size="md"
            :trailing-icon="error ? 'i-heroicons-exclamation-triangle-20-solid' : undefined" 
            :ui="{
              rounded: 'rounded',
              color: error ?
                { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : 
                { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
            }" />
        </template>

        <template #error="{ error }">
          <span
            :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
            {{ error ? error : undefined }}
          </span>
        </template>
      </UFormGroup>

      <UButton 
        type="submit" 
        :label="label" 
        :loading-icon="loadIcon" 
        :loading="loading"
        class="flex justify-center items-center gap-1 py-2 rounded dark:text-custom-50 dark:bg-custom-500 hover:dark:bg-custom-500/75" />

    </UForm>
  </div>
</template>

<script setup lang="ts">
import { user } from '~/assets/js/userLogged';
import type { FormError, FormErrorEvent, FormSubmitEvent } from '#ui/types'
import { name, playSound } from '~/assets/js/sound'

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

const toast = useToast()
name.value = 'login_1'

const showToast = () => {
  playSound()

  toast.add({
    title: 'Login Successfully!',
    icon: 'i-lucide-log-out',
    timeout: 2000,
    ui: {
      background : 'dark:bg-green-700 bg-green-300', 
      progress: {
        background: 'dark:bg-white bg-green-700 rounded-full'
      }, 
      ring: 'ring-1 ring-green-700 dark:ring-custom-900',
      default: {
        closeButton: { 
          color: 'white',
        }
      },
      icon: 'text-custom-900'
    },
  })
}

async function onSubmit(event: FormSubmitEvent<any>) {
  // Do something with data
  console.log(event.data)

  loading.value = true;
  loadIcon.value = 'i-lucide-loader-circle';
  label.value = '';

  setTimeout(() => {
    console.log(user.role);

    if (user.role === 'client') {
      showToast()
      navigateTo('/client/monitor');
    } else if (user.role === 'admin' || user.role === 'superadmin') {
      showToast()
      navigateTo('/admin/dashboard');
    } else {
      alert('Unrecognized role detected! Please contact an Admin for verification.');
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
