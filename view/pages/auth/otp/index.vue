<template>

<UseHead title="Verification - Auth" description="OTP Authentication adds an extra layer of security by requiring a one-time password for each login or transaction, enhancing protection against unauthorized access." />

<div class="flex justify-center items-center h-screen w-auto">

    <ToggleDarkMode class="fixed sm:top-20 z-50 top-3 left-3 sm:left-20 duration-200" />

    <main class="h-auto w-[500px] flex flex-col gap-4 rounded p-8 bg-custom-50 dark:bg-custom-900 shadow-lg border dark:border-custom-700 border-custom-300">
        <header>
            <div class="flex items-center justify-end">
            <UButton icon="i-lucide-x" @click="goBack"
                class="flex justify-center items-center text-sm rounded-full dark:bg-red-600 dark:hover:bg-red-600/75 bg-red-600 hover:bg-red-600/75 dark:text-custom-100"
                size="2xs" />
            </div>
            <h1 class="text-2xl font-bold cursor-default text-center">Verify your Identity</h1>
        </header>

        <hr class="border-custom-300 dark:border-custom-500">
        
        <!-- sms -->
        <UButton
            label="SMS Verification"
            icon="i-lucide-message-square-more"
            :loading="loadingSMS"
            :loading-icon="loadIconSMS"
            class="flex justify-center items-center gap-1 py-2 rounded dark:text-custom-50 dark:bg-custom-500 hover:dark:bg-custom-500/75"
            @click="sms" />

        <!-- email -->
        <UButton
            label="Email Verification"
            icon="i-lucide-mail"
            :loading="loadingEmail"
            :loading-icon="loadIconEmail"
            class="flex justify-center items-center gap-1 py-2 rounded dark:text-custom-50 dark:bg-custom-500 hover:dark:bg-custom-500/75"
            @click="email" />
    </main>
</div>
</template>

<script setup>

const loadingSMS = ref(false);
const loadIconSMS = ref('');

const loadingEmail = ref(false);
const loadIconEmail = ref('');

const sms = () => {
    loadingSMS.value = true;
    loadIconSMS.value = 'i-lucide-loader-circle'

    setTimeout(() => {
    navigateTo('/auth/otp/sms');
    loadingSMS.value = false;
    }, 800);
};

const email = () => {
    loadingEmail.value = true;
    loadIconEmail.value = 'i-lucide-loader-circle'

    setTimeout(() => {
    navigateTo('/auth/otp/email');
    loadingEmail.value = false;
    }, 800);
};

const router = useRouter();

const goBack = () => {
    router.go(-1);  
};
</script>