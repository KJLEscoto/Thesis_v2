<template>

<UseHead title="Email - Auth" description="Email verification." />

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
        <UButton 
            icon="i-lucide-x" 
            to="/auth/otp"
            class="flex justify-center items-center text-sm rounded-full dark:bg-red-600 dark:hover:bg-red-600/75 bg-red-600 hover:bg-red-600/75 dark:text-custom-100"
            size="2xs" />
        </div>
        <div class="flex justify-center items-center gap-1">
        <UIcon 
            name="i-lucide-mail" 
            class="text-3xl" />
        <h1 class="text-2xl font-bold cursor-default">Email Verification</h1>
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
            <p class="font-normal">Enter the code from the <strong>Email</strong> we sent to</p>
            <p class="font-medium text-base italic text-blue-700 dark:text-blue-500">{{ user.email }}</p>
        </div>
        </template>

        <template #default="{ error }">
        <UInput 
            v-model="state.otp" 
            placeholder="6-digit pin"
            type="text" 
            color="gray" 
            size="md"
            :trailing-icon="error ? 'i-heroicons-exclamation-triangle-20-solid' : ''" 
            :ui="{
            rounded: 'rounded',
            color: error ?
                { red: { outline: 'dark:bg-red-50 bg-red-100 dark:text-custom-900 focus:ring-2 ring-1 ring-red-400 focus:ring-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : 
                { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900 border-none' } }
            }" />
        </template>

        <template #error="{ error }">
        <span
            :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
            {{ error ? error : '' }}
        </span>
        </template>
    </UFormGroup>

    <UButton 
        type="submit" 
        :label="load.label.value" 
        :loading-icon="load.icon.value" 
        :loading="load.bool.value"
        class="flex justify-center items-center gap-1 py-2 rounded dark:text-custom-50 dark:bg-custom-500 hover:dark:bg-custom-500/75" />

    </UForm>
</div>
</template>

<script setup lang="ts">
import { user, fetchUser } from '~/assets/js/userLogged';
import type { FormError, FormErrorEvent, FormSubmitEvent } from '#ui/types'
import { name, playSound } from '~/assets/js/sound'

const loadUser = async () => {
    await fetchUser();
    // console.log(user);
}

onMounted(() => {
    loadUser() // Load user data when the component mounts
})

const state = reactive({
    otp: ''
})

// FE validation
const validate = (state: any): FormError[] => {
    const errors = []
    if (!state.otp) errors.push({ path: 'otp', message: 'Required' })
    return errors
}

// input field focus
async function onError(event: FormErrorEvent) {
    const element = document.getElementById(event.errors[0].id)
    element?.focus()
    element?.scrollIntoView({ behavior: 'smooth', block: 'center' })
}

const load = {
    bool: ref(false),
    label: ref('Submit'),
    icon: ref('')
}

async function onSubmit(event: FormSubmitEvent<any>) {
    // console.log(event.data)

    load.bool.value = true;
    load.icon.value = 'i-lucide-loader-circle';
    load.label.value = '';

    // sound
    name.value = 'login_1'

    const toast = useToast()

    const showToast = () => {
        toast.add({
            title: 'Login Successfully!',
            icon: 'i-lucide-log-in',
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
        playSound()
    }

    setTimeout(() => {
        // console.log(user.role);

        // Conditional navigation based on user role
        if (user.role === 'client') {
            navigateTo('/client/monitor');
            showToast()
        } else if (user.role === 'admin' || user.role === 'superadmin') {
            navigateTo('/admin/dashboard');
            showToast()
        } else {
            alert('Unrecognized role detected! Please contact support.');
        }

        load.label.value = 'Submit';
        load.bool.value = false;
    }, 800);
}

</script>
