<template>
  <div class="flex justify-center items-center h-screen w-auto">
    <ToggleDarkMode class="fixed sm:top-20 z-50 top-3 left-3 sm:left-20 duration-200"/>
    <div class="h-auto lg:w-1/3 sm:w-1/2 w-full duration-150 rounded p-10 sm:bg-custom-50 bg-inherit dark:sm:bg-custom-900 dark:bg-inherit sm:shadow-lg shadow-none">
      <header class="flex items-center justify-center gap-1">
        <UIcon name="i-lucide-shield-check" class="text-3xl"/>
        <h1 class="text-2xl font-bold cursor-default">Client Auth</h1>
      </header>
      <hr class="mt-5 mb-5 border-custom-300">

      <UForm :state="state" class="grid gap-5">

        <section>
          <label class="font-semibold flex gap-1 justify-start items-center" for="username">
            <UIcon name="i-lucide-user-round"/>
            <p>Username</p>
          </label>
          <input placeholder="Enter username" type="text" id="username"
            class="w-full bg-custom-50 py-2 px-3 rounded border-2 border-custom-200 transition-all duration-300 outline-none focus:border-custom-700 dark:focus:border-custom-50 mt-1 text-custom-900"/>
        </section>

        <section>
          <label class="font-semibold flex gap-1 justify-start items-center" for="password">
            <UIcon name="i-lucide-key-round"/>
            <p>Password</p>
          </label>
          <input placeholder="••••••••" type="password" id="password"
            class="w-full bg-custom-50 py-2 px-3 rounded border-2 border-custom-200 transition-all duration-300 outline-none focus:border-custom-700 dark:focus:border-custom-50 mt-1 text-custom-900"/>
        </section>

        <UButton :label="labelClient" class="w-full items-center justify-center font-bold flex py-3 rounded dark:text-custom-200" @click="clientLogin" :loading="loading" :loading-icon="loadIcon"/>

        <Divider />

        <UButton to="/login/as-admin" label="Continue as Admin" icon="i-lucide-square-user-round" class="flex justify-center items-center gap-1 py-3 rounded bg-custom-700 hover:bg-custom-800 dark:bg-custom-600 dark:hover:bg-custom-700 dark:text-custom-200"/>

      </UForm>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { user as userRole } from '~/assets/js/userRole';

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
    userRole.role = 'client';
    
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
