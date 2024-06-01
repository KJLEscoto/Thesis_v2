<template>
  <div class="h-screen w-full flex flex-col p-5 gap-5">
    <section class="">
      <UBreadcrumb :links="links">    
        <template #divider>
          <UIcon name="i-lucide-chevron-right" class="text-lg"/>
        </template>
        <template #default="{ link, isActive }">
          <div :class="{'dark:text-white text-custom-800 text-lg cursor-default': isActive, 'text-custom-300 hover:text-custom-500 hover:dark:text-custom-300 dark:text-custom-500 text-lg': !isActive}" class="rounded-full">
            {{ link.label }}
          </div>
        </template>
      </UBreadcrumb>
    </section>
    <section class="h-4/5 w-full flex justify-center items-center">
      <div class="sm:w-3/4 w-full h-auto">

          <UForm class="h-auto w-full flex flex-col gap-3" :state="state">
            <header class="flex justify-between items-center">
              <div class="font-semibold cursor-default flex items-center gap-1 w-1/2">
                <UIcon name="i-lucide-user-round-plus" class="text-xl" />
                <h1 class="font-bold text-xl">New User</h1>
              </div>
            </header>

            
            <div class="flex justify-between">
              <h1 class="text-lg w-auto">Personal Information</h1>
            
              <div class="flex justify-end w-1/2 gap-x-2">
                <section class="w-auto">
                  <UButton 
                    label="Cancel" 
                    icon="i-lucide-x"
                    class="flex justify-center w-full items-center rounded dark:bg-red-600 dark:hover:bg-red-500 bg-red-700 hover:bg-red-600 dark:text-custom-100" 
                    to="/admin/users"
                  />
                </section>
                <section class="w-auto">
                  <UButton 
                    label="Save" 
                    icon="i-lucide-save"
                    class="flex justify-center w-full items-center rounded dark:text-white" 
                    type="submit" 
                  />
                </section>
              </div>
            </div>

            <hr class="border-custom-300 dark:border-custom-500 w-full">


            <section class="grid grid-cols-5 gap-3">
              <UFormGroup class="grid col-span-2" label="First name">
                <UInput type="text" color="gray" size="sm" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
              </UFormGroup>
              <UFormGroup class="grid col-span-2" label="Last name">
                <UInput type="text" color="gray" size="sm" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
              </UFormGroup>
              <UFormGroup class="grid col-span-1" label="M. I.">
                <UInput type="text" color="gray" size="sm" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
              </UFormGroup>
              <UFormGroup class="grid col-span-2" label="Gender">
                <URadioGroup v-model="selectedGender" :options="genderOptions" class="ml-2" />
              </UFormGroup>
              <UFormGroup class="grid col-span-3">
                <template #label>
                  <div class="flex items-center justify-start gap-1">
                    <p class="text-base">Phone no.</p>
                    <UIcon name="i-emojione-v1-flag-for-philippines" />
                  </div>
                </template>
                <UInput type="text" color="gray" size="sm" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
              </UFormGroup>
              <UFormGroup class="grid col-span-2" label="Status">
                <URadioGroup v-model="selectedStatus" :options="statusOptions" class="ml-2" :uiRadio="radioGroupUI" />
              </UFormGroup><UFormGroup class="grid col-span-3" label="Role">
                <UInputMenu color="gray" :ui="{rounded: 'rounded', color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" 
                  :uiMenu="{background: 'dark:bg-custom-400', option: {color: 'dark:text-white', active: 'dark:bg-custom-600', empty: 'dark:text-white'}, empty: 'dark:text-white'}" 
                  v-model="selectedRole" :options="roleOptions" placeholder="Select a role" />
              </UFormGroup>
            </section>

            <h1 class="text-lg w-auto text-start mt-3 -mb-2">Login Credentials</h1>
            <hr class="border-custom-300 dark:border-custom-500 w-full">

            <section class="grid grid-cols-2 gap-3">
              <UFormGroup class="" label="Username">
                <UInput type="text" color="gray" size="sm" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
              </UFormGroup>
              <UFormGroup class="" label="Password">
                <UInput type="password" color="gray" size="sm" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
              </UFormGroup>
            </section>
          </UForm>
      </div>
    </section>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'sidebar'
})

const state = reactive({
  first_name: '',
  gender: undefined,
  email: undefined,
  password: undefined
});

const selectedRole = ref('');
const selectedStatus = ref('Active');
const selectedGender = ref('');

const roleOptions = ['Admin', 'Client'];
const statusOptions = ['Active', 'Inactive'];
const genderOptions = ['Male', 'Female'];

const radioGroupUI = computed(() => ({
  color: selectedStatus.value === statusOptions[0] ? 'text-green-500' : 'text-red-500'
}));

const links = [{
  label: 'Users',
  to: '/admin/users'
}, {
  label: 'Create',
}]
</script>
