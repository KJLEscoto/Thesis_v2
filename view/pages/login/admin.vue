<template>
  <div class="flex justify-center items-center h-screen w-auto">

    <ToggleDarkMode class="fixed lg:top-20 z-50 top-5 left-5 lg:left-20 duration-200"/>

      <UForm :state="state" class="h-auto w-[500px] flex flex-col gap-5 rounded p-8 bg-custom-50 dark:bg-custom-900 shadow-lg">

        <header class="flex items-center justify-between">
          <UButton label="Back" icon="i-lucide-corner-up-left" to="/login/client" class="flex justify-center items-center text-sm rounded dark:bg-red-600 dark:hover:bg-red-500 bg-red-700 hover:bg-red-600 dark:text-custom-100" size="2xs"/>
          <div class="flex justify-end items-center gap-1">
            <UIcon name="i-lucide-circle-user-round" class="text-3xl"/>
            <h1 class="text-xl font-bold cursor-default">Admin</h1>
          </div>
        </header>

        <hr class="border-custom-300 dark:border-custom-500">

        <UFormGroup class="grid gap-1">
          <template #label>
            <div class="flex items-center justify-start gap-1">
              <UIcon name="i-lucide-user-round" class="text-lg"/>
              <p class="text-base">Username</p>
            </div>
          </template>
          <UInput type="text" color="gray" size="md" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" placeholder="Enter username"/>
        </UFormGroup>

        <UFormGroup class="grid gap-1">
          <template #label>
            <div class="flex items-center justify-start gap-1">
              <UIcon name="i-lucide-key-round" class="text-lg"/>
              <p class="text-base">Password</p>
            </div>
          </template>
          <UInput type="password" color="gray" size="md" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" placeholder="••••••••"/>
        </UFormGroup>

        <UButton @click="adminLogin" :label="labelAdmin" :loading-icon="loadIcon" :loading="loading" class="flex justify-center items-center gap-1 py-2 rounded bg-custom-700 hover:bg-custom-800 dark:bg-custom-600 dark:hover:bg-custom-700 dark:text-custom-200"/>

      </UForm>

    </div>

</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { user as userRole } from '~/assets/js/userRole';

const state = reactive({
  email: '',
  password: ''
});

const loading = ref(false);
const router = useRouter();
const loadIcon = ref('');
const labelAdmin = ref('Login');

const adminLogin = () => {
  loading.value = true;
  loadIcon.value = 'i-lucide-loader-circle';
  labelAdmin.value = '';
  setTimeout(() => {
    userRole.role = 'superadmin';
    router.push('/admin/dashboard');
    labelAdmin.value = 'Login';
    loading.value = false;
  }, 800);
};

</script>