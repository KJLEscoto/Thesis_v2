<template>

    <UseHead :title="`Edit - ${user.username} - Users - Admin`"/>

<div class="h-auto w-full flex flex-col p-5 gap-10">
    <section class="">
    <UBreadcrumb :links="links">
        <template #divider>
        <UIcon name="i-lucide-chevron-right" class="text-lg" />
        </template>
        <template #default="{ link, isActive }">
        <div :class="{
            'dark:text-white text-custom-800 text-lg cursor-default': isActive,
            'text-custom-300 hover:text-custom-500 hover:dark:text-custom-300 dark:text-custom-500 text-lg': !isActive
        }" class="rounded-full">
            {{ link.label }}
        </div>
        </template>
    </UBreadcrumb>
    </section>
    <section class="h-4/5 w-full flex justify-center items-center">
    <div
        class="sm:w-3/4 w-full h-auto border p-5 rounded border-custom-300 bg-custom-100 dark:bg-custom-900 dark:border-custom-700">

        <UForm class="h-auto w-full flex flex-col gap-3" :state="state" @submit="onSubmit" :validate="validate"
        @error="onError">

        <header class="flex justify-between items-center">
            <div class="font-semibold cursor-default flex items-center gap-1 w-1/2">
            <UIcon name="i-lucide-edit" class="text-xl" />
            <h1 class="font-bold text-xl">Edit User</h1>
            </div>
        </header>

        <div class="flex justify-between">

            <h1 class="text-lg w-auto font-medium">Personal Information</h1>

            <div class="flex justify-end w-1/2 gap-x-2">

            <section class="w-auto">
                <UButton label="Cancel" icon="i-lucide-x"
                class="flex justify-center w-full items-center rounded dark:bg-red-600 dark:hover:bg-red-500 bg-red-700 hover:bg-red-600 dark:text-custom-100"
                :to="`/admin/users/${user.username}`"/>
            </section>

            <section class="w-auto">
                <UButton :label="label" :loading-icon="loadIcon" :loading="loading" icon="i-lucide-save"
                class="flex justify-center w-full items-center rounded dark:text-white" type="submit" />
            </section>
            </div>
        </div>

        <hr class="border-custom-300 dark:border-custom-500 w-full">

        <section class="flex w-full gap-x-2">

            <!-- first name -->
            <UFormGroup class="w-1/2" label="First name" name="first_name" :ui="{ error: 'mt-1' }">

            <template #default="{ error }">
                <UInput type="text" color="gray" v-model="state.first_name" size="md" :ui="{
                rounded: 'rounded',
                color: error ?
                    { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
                }" />
            </template>

            <template #error="{ error }">
                <span
                :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
                </span>
            </template>
            </UFormGroup>

            <!-- last name -->
            <UFormGroup class="w-1/2" label="Last name" name="last_name" :ui="{ error: 'mt-1' }">

            <template #default="{ error }">
                <UInput type="text" color="gray" v-model="state.last_name" size="md" :ui="{
                rounded: 'rounded',
                color: error ?
                    { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
                }" />
            </template>

            <template #error="{ error }">
                <span
                :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
                </span>
            </template>
            </UFormGroup>

            <!-- middle initial -->
            <UFormGroup class="w-1/4" label="M. I." name="m_i">
            <template #default="{ error }">
                <UInput type="text" color="gray" size="md" v-model="state.m_i" :ui="{
                rounded: 'rounded',
                color: error ?
                    { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900 py-2' } }
                }" />
            </template>
            <template #error="{ error }">
                <span
                :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
                </span>
            </template>
            </UFormGroup>
        </section>

        <section class="flex w-full gap-x-2">
        <!-- phone -->
        <UFormGroup class="w-1/2" name="phone">
            <template #label>
            <div class="flex items-center justify-start gap-1">
                <p class="text-sm">Phone no.</p>
                <UIcon name="i-emojione-v1-flag-for-philippines" />
            </div>
            </template>
            <template #default="{ error }">
            <UInput type="text" color="gray" size="md" v-model="state.phone" :ui="{
                rounded: 'rounded',
                color: error ?
                { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
            }" />
            </template>
            <template #error="{ error }">
            <span
                :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
            </span>
            </template>
        </UFormGroup>

        <!-- email -->
        <UFormGroup class="w-1/2" name="email">
            <template #label>
            <p class="text-sm">Email</p>
            </template>
            <template #default="{ error }">
            <UInput type="email" color="gray" size="md" v-model="state.email" :ui="{
                rounded: 'rounded',
                color: error ?
                { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
            }" />
            </template>
            <template #error="{ error }">
            <span
                :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
            </span>
            </template>
        </UFormGroup>

        <!-- gender -->
        <UFormGroup class="w-1/4" label="Gender" name="gender">
            <URadioGroup v-model="state.gender" :options="genderOptions" class="ml-2" />
            <template #error="{ error }">
            <span
                :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
            </span>
            </template>
        </UFormGroup>
        </section>

        <section class="flex w-full gap-x-2">

            <!-- role -->
            <UFormGroup class="w-full" label="Role" name="role">
            <template #default="{ error }">
                <USelectMenu disabled color="gray" size="md" :ui="{
                rounded: 'rounded',
                color: error ?
                    { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
                }"
                :uiMenu="{ background: 'dark:bg-custom-400', option: { color: 'dark:text-white', active: 'dark:bg-custom-600', empty: 'dark:text-white' }, empty: 'dark:text-white' }"
                v-model="state.role" placeholder="Select a role" />
            </template>
            <template #error="{ error }">
                <span
                :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
                </span>
            </template>
            </UFormGroup>

            <!-- status -->
            <UFormGroup class="w-1/4" label="Status" name="status">
            <URadioGroup v-model="state.status" :options="statusOptions" class="ml-2"
                :uiRadio="{ color: state.status === statusOptions[0].value ? 'text-green-500' : 'text-red-500' }" />
            </UFormGroup>

        </section>

        <h1 class="text-lg w-auto text-start mt-3 -mb-2 font-medium">Login Credentials</h1>
        <hr class="border-custom-300 dark:border-custom-500 w-full">

        <section class="flex w-full gap-x-2">

            <!-- username -->
            <UFormGroup class="w-1/2" label="Username" name="username">
            <template #default="{ error }">
                <UInput type="text" color="gray" size="md" v-model="state.username" :ui="{
                rounded: 'rounded',
                color: error ?
                    { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
                }" />
            </template>
            <template #error="{ error }">
                <span
                :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
                </span>
            </template>
            </UFormGroup>

            <!-- password -->
            <UFormGroup class="w-1/2" label="Password" name="password">
            <template #default="{ error }">
                <UInput type="password" color="gray" size="md" v-model="state.password" :ui="{
                rounded: 'rounded',
                color: error ?
                    { red: { outline: 'bg-red-100 dark:bg-red-50 text-custom-900 dark:text-custom-900 focus:ring-1 focus:ring-red-400 border-2 border-red-400 focus:border-red-400 active:ring-red-400 active:border-red-400' } } : { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }
                }" />
            </template>
            <template #error="{ error }">
                <span
                :class="[error ? 'text-red-500 dark:text-red-400 text-xs font-bold' : 'text-primary-500 dark:text-primary-400']">
                {{ error ? error : undefined }}
                </span>
            </template>
            </UFormGroup>

        </section>
        </UForm>
    </div>
    </section>
</div>
</template>

<script setup lang="ts">
definePageMeta({
layout: 'sidebar'
})

import { name, playSound } from '~/assets/js/sound'
import type { FormError, FormErrorEvent, FormSubmitEvent } from '#ui/types'
import { user } from '~/assets/js/userLogged';

const statusOptions = [
{
    value: 'active',
    label: 'Active'
},
{
    value: 'inactive',
    label: 'Inactive'
}
];

const genderOptions = [
{
    value: 'male',
    label: 'Male'
},
{
    value: 'female',
    label: 'Female'
}
];

const state = reactive({
    first_name: user.first_name,
    last_name: user.last_name,
    m_i: user.mi,
    gender: user.gender,
    status: user.status,
    phone: user.phone,
    role: user.role,
    username: user.username,
    password: user.password,
    email: user.email
})

const validate = (state: any): FormError[] => {
const errors = []
if (!state.first_name) errors.push({ path: 'first_name', message: 'Required' })
if (!state.last_name) errors.push({ path: 'last_name', message: 'Required' })
if (!state.gender) errors.push({ path: 'gender', message: 'Required' })
if (!state.phone) errors.push({ path: 'phone', message: 'Required' })
if (!state.status) errors.push({ path: 'status', message: 'Required' })
if (!state.username) errors.push({ path: 'username', message: 'Required' })
if (!state.password) errors.push({ path: 'password', message: 'Required' })
return errors
}

const loading = ref(false);
const loadIcon = ref('');
const label = ref('Update');

const toast = useToast()


async function onSubmit(event: FormSubmitEvent<any>) {
// Do something with data
console.log(event.data)

loading.value = true;
loadIcon.value = 'i-lucide-loader-circle';
label.value = '';
name.value = 'success_1'

setTimeout(() => {
    playSound()
    toast.add({
        title: 'Updated Successfully!',
        icon: 'i-lucide-circle-check-big',
        timeout: 2500,
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
    label.value = 'Update';
    loading.value = false;
    navigateTo(`/admin/users/${user.username}`)
}, 800)
}

async function onError(event: FormErrorEvent) {
const element = document.getElementById(event.errors[0].id)
element?.focus()
element?.scrollIntoView({ behavior: 'smooth', block: 'center' })
}

const links = [{
label: 'Users',
to: '/admin/users'
}, {
label: 'Details',
to: `/admin/users/${user.username}`
}, {
label: 'Update',
}
]
</script>
