<template>
  <div class="flex justify-center items-center h-screen w-auto">
    <ToggleDarkMode class="fixed sm:top-20 z-50 top-3 left-3 sm:left-20 duration-200"/>

    <UForm 
      :state="state" 
      class="h-auto w-[500px] flex flex-col gap-5 rounded p-8 bg-custom-50 dark:bg-custom-900 shadow-lg"
    >

      <header class="flex items-center justify-center gap-1">
        <UIcon 
          name="i-lucide-shield-check" 
          class="text-3xl"
        />
        <h1 class="text-2xl font-bold cursor-default">Client Auth</h1>
      </header>

      <hr class="border-custom-300 dark:border-custom-500">

      <UFormGroup class="grid gap-1">
        <template #label>
          <div class="flex items-center justify-start gap-1">
            <UIcon 
              name="i-lucide-user-round" 
              class="text-lg"
            />
            <p class="text-base">Username</p>
          </div>
        </template>
        <UInput 
          type="text" 
          color="gray" 
          size="md" 
          :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" 
          placeholder="Enter username"
        />
      </UFormGroup>

      <UFormGroup class="grid gap-1">
        <template #label>
          <div class="flex items-center justify-start gap-1">
            <UIcon 
              name="i-lucide-key-round" 
              class="text-lg"
            />
            <p class="text-base">Password</p>
          </div>
        </template>
        <UInput 
          type="password" 
          color="gray" 
          size="md" 
          :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" 
          placeholder="••••••••"
        />
      </UFormGroup>

      <UButton 
        @click="clientLogin" 
        :label="labelClient" 
        :loading-icon="loadIcon" 
        :loading="loading" 
        class="flex justify-center items-center gap-1 py-2 rounded dark:text-custom-50"
      />

      <Divider />

      <UButton 
        to="/login/admin" 
        label="Continue as Admin" 
        icon="i-lucide-square-user-round" 
        class="flex justify-center items-center gap-1 py-2 rounded bg-custom-700 hover:bg-custom-800 dark:bg-custom-600 dark:hover:bg-custom-700 dark:text-custom-50"
      />

      </UForm>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { user } from '~/assets/js/userRole';

const loading = ref(false);
const router = useRouter();
const loadIcon = ref('');
const labelClient = ref('Login');

const clientLogin = () => {
  loading.value = true;
  loadIcon.value = 'i-lucide-loader-circle';
  labelClient.value = '';

  // Simulate login process
  setTimeout(() => {
    // Update usertype in the userType module
    user.role = 'client';
    
    // Navigate to client monitor page
    router.push('/client/monitor');
    
    // Reset button label and loading state
    labelClient.value = 'Login';
    loading.value = false;
  }, 800);
};

const state = reactive({
  email: undefined,
  password: undefined
});

</script>
