<template>
  <div class="flex justify-center items-center h-screen w-auto">
    <ToggleDarkMode class="fixed lg:top-20 z-50 top-5 left-5 lg:left-20 duration-200"/>
    <div class="h-auto w-1/3 rounded p-10 bg-custom-100 dark:bg-custom-900 shadow-lg">
      <header class="flex items-center justify-center gap-1">
        <UIcon name="i-lucide-shield-check" class="text-3xl"/>
        <h1 class="text-2xl font-bold cursor-default">Authentication</h1>
      </header>
      <hr class="mt-5 mb-5 border-custom-300">
      <UForm :state="state" class="grid gap-5">

        <section id="username">
          <label class="font-semibold flex gap-1 justify-start items-center">
            <UIcon name="i-lucide-user-round"/>
            <p>Username</p>
          </label>
          <input placeholder="Enter username" type="text"
            class="w-full bg-custom-50 py-2 px-3 rounded border-2 border-custom-200 transition-all duration-300 outline-none focus:border-custom-700 dark:focus:border-custom-50 mt-1 text-custom-900"/>
        </section>

        <section id="username">
          <label class="font-semibold flex gap-1 justify-start items-center">
            <UIcon name="i-lucide-key-round"/>
            <p>Password</p>
          </label>
          <input placeholder="Enter password" type="password"
            class="w-full bg-custom-50 py-2 px-3 rounded border-2 border-custom-200 transition-all duration-300 outline-none focus:border-custom-700 dark:focus:border-custom-50 mt-1 text-custom-900"/>
        </section>

        <UButton :label="labelClient" class="w-full items-center justify-center font-bold flex py-3 rounded dark:text-white" @click="clientLogin" :loading="loading" :loading-icon="loadIcon"/>

        <Divider />

        <UButton to="/login/as-admin" label="Continue as Admin" icon="i-lucide-square-user-round" class="flex justify-center items-center gap-1 py-3 rounded bg-custom-700 hover:bg-custom-800 dark:bg-custom-600 dark:hover:bg-custom-700 dark:text-white"/>

      </UForm>
    </div>
  </div>
</template>

<script setup>

const loading = ref(false);
const router = useRouter();
const loadIcon = ref('');
const labelClient = ref('Login');

const clientLogin = () => {
  loading.value = true;
  loadIcon.value = 'i-lucide-loader-circle';
  labelClient.value = '';
  setTimeout(() => {
    router.push('/client/monitor');
    labelClient.value = 'Login';
    loading.value = false;
  }, 800);
};

const state = reactive({
  email: undefined,
  password: undefined
})

</script>