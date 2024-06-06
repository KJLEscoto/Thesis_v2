<template>
  <div class="h-screen w-full flex flex-col p-5 gap-5">
    <section class="">
      <UBreadcrumb :links="links">    
        <template #divider>
          <UIcon 
            name="i-lucide-chevron-right" 
            class="text-lg" />
        </template>
        <template #default="{ link, isActive }">
          <div 
            :class="{'dark:text-white text-custom-800 text-lg cursor-default': isActive, 
            'text-custom-300 hover:text-custom-500 hover:dark:text-custom-300 dark:text-custom-500 text-lg': !isActive}" 
            class="rounded-full" >
            {{ link.label }}
          </div>
        </template>
      </UBreadcrumb>
    </section>
    <section class="h-4/5 w-full flex justify-center items-center">
      <div class="sm:w-3/4 w-full h-auto flex flex-col gap-5">
        <div class="flex justify-between">
                
          <div class="font-semibold cursor-default flex items-center gap-1 w-1/2">
            <UIcon 
              name="i-lucide-book-user" 
              class="text-xl" />
            <h1 class="font-bold text-xl">User Details</h1>
          </div>
          
            <div class="flex justify-end w-1/2 gap-x-2">
              <section class="w-auto">
                <UButton 
                  label="Back" 
                  icon="i-lucide-move-left"
                  class="flex justify-center w-full items-center rounded dark:bg-red-600 dark:hover:bg-red-500 bg-red-700 hover:bg-red-600 dark:text-custom-100" 
                  to="/admin/users" />
              </section>
              <section class="w-auto">
                <UButton 
                  label="Edit" 
                  class="flex justify-center w-full items-center rounded dark:text-white"
                  icon="i-lucide-edit"
                  to="/admin/users/read/update/1" />
              </section>
            </div>
          </div>

        <div class="grid lg:grid-cols-2 grid-cols-1 gap-3">
          <section class="bg-custom-100 dark:bg-custom-900 rounded p-5 lg:row-span-2 row-span-1">
            <h1 class=" font-semibold">Personal Information</h1>
            <hr class="border-custom-200 dark:border-custom-700 mt-2 mb-2">
            <div class="grid grid-cols-4 gap-2 mt-1 text-sm">
              <h1 class="col-span-1">Name:</h1>
              <p class="col-span-3">{{ props.clientData.name }}</p>

              <h1 class="col-span-1">Gender:</h1>
              <p class="col-span-3">{{ props.clientData.gender }}</p>

              <h1 class="col-span-1">Phone:</h1>
              <p class="col-span-3">{{ props.clientData.phone }}</p>

              <h1 class="col-span-1">Role:</h1>
              <p class="col-span-3">{{ props.clientData.role }}</p>

              <h1 class="col-span-1">Status:</h1>
              <p class="col-span-3">{{ props.clientData.status }}</p>
            </div>
          </section>
          <div class="grid row-span-2 gap-3">
            <section class="bg-custom-100 dark:bg-custom-900  rounded p-5">
              <h1 class=" font-semibold">Login Credentials</h1>
              <hr class="border-custom-200 dark:border-custom-700 mt-2 mb-2">
              <div class="grid grid-cols-3 gap-2 text-sm">
                <h1 class="col-span-1">Username:</h1>
                <p class="col-span-2">{{ props.clientData.username }}</p>

                <h1 class="col-span-1">Password:</h1>
                <p class="col-span-2">...</p>
              </div>
            </section>
            <section class="bg-custom-100 dark:bg-custom-900  rounded p-5">
              <h1 class=" font-semibold">Timestamps (date & time)</h1>
              <hr class="border-custom-200 dark:border-custom-700 mt-2 mb-2">
              <div class="grid grid-cols-5 gap-2 mt-1 text-sm">
                <h1 class="col-span-2">Account Created:</h1>
                <p class="col-span-3">...</p>

                <h1 class="col-span-2">Last Updated:</h1>
                <p class="col-span-3">...</p>
              </div>
            </section>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'sidebar'
});

const links = [{
  label: 'Users',
  to: '/admin/users'
}, {
  label: 'Read'
}];

const props = defineProps({
  clientData: {
    type: Object,
    default: () => ({})
  }
});
</script>
