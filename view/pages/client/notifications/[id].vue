<template>
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
      <div class="sm:w-3/4 w-full h-auto flex flex-col gap-5">
        <div class="flex justify-between">

          <div class="font-semibold cursor-default flex items-center gap-1 w-1/2">
            <UIcon name="i-lucide-book-open-text" class="text-xl" />
            <h1 class="font-bold text-xl">Notification Details</h1>
          </div>

          <div class="flex justify-end w-1/2 gap-x-2">
            <section class="w-auto">
              <UButton label="Back" icon="i-lucide-move-left"
                class="flex justify-center w-full items-center rounded dark:bg-red-600 dark:hover:bg-red-500 bg-red-700 hover:bg-red-600 dark:text-custom-100"
                to="/client/notifications" />
            </section>
          </div>
        </div>

        <p>-- retrieve ang info sa notifications gamit ang ID --</p>

        <div class="lg:flex grid gap-5 w-full">
          <section
            class="bg-custom-100 dark:bg-custom-900 border border-custom-300 dark:border-custom-700 rounded p-5 lg:w-1/2 w-full">
            <h1 class=" font-semibold">Motion Detected</h1>
            <hr class="border-custom-200 dark:border-custom-700 mt-2 mb-2">
            <section class="my-auto">
              <div v-for="(m, index) in motion" :key="index" class="grid grid-cols-3 gap-5 my-2">
                <h1 class="capitalize col-span-1">{{ m.label }}: </h1>
                <div class="col-span-2 dark:text-custom-300 text-custom-500 capitalize">
                  <UKbd v-if="m.label === 'level'" :class="{
                    'dark:border bg-green-600 dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default px-2': m.value === 'normal',
                    'dark:border bg-red-600 dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default px-2': m.value === 'danger'
                  }" :value="m.value" />
                  <p v-else> {{ m.value }} </p>
                </div>

              </div>
            </section>
          </section>
          <div class="flex flex-col gap-5 lg:w-1/2 w-full">
            <UForm class="h-auto w-full flex flex-col gap-3" :state="state" @submit="onSubmit" :validate="validate"
              @error="onError">
              <section
                class="bg-custom-100 dark:bg-custom-900 rounded p-5 border border-custom-300 dark:border-custom-700">
                <div class="flex justify-between items-center">
                  <h1 class=" font-semibold">Status</h1>
                  <section class="w-auto">
                    <UButton :label="label" :loading-icon="loadIcon" :loading="loading" icon="i-lucide-save"
                      class="flex justify-center w-full items-center rounded dark:text-white" type="submit" size="xs" />
                  </section>
                </div>
                <hr class="border-custom-200 dark:border-custom-700 mt-2 mb-2">
                <section class="my-auto">
                  <!-- status -->

                  <UFormGroup class="w-2/3" name="status">
                    <URadioGroup v-model="state.status" :options="statusOptions" class="ml-2"
                      :uiRadio="{ color: state.status === statusOptions[0].value ? 'text-green-500' : 'text-orange-500' }" />
                  </UFormGroup>
                </section>
              </section>
            </UForm>
            <section
              class="bg-custom-100 dark:bg-custom-900 rounded p-5 border border-custom-300 dark:border-custom-700">
              <h1 class=" font-semibold">Timestamps (date & time)</h1>
              <hr class="border-custom-200 dark:border-custom-700 mt-2 mb-2">
              <section class="my-auto">
                <div v-for="(t, index) in timestamp" :key="index" class="grid grid-cols-5 gap-5 my-2">
                  <h1 class="capitalize col-span-2">{{ t.label }}: </h1>
                  <p class="col-span-3 dark:text-custom-300 text-custom-500 capitalize">{{ t.value }}</p>
                </div>
              </section>
            </section>
          </div>
        </div>

        <div
          class="flex justify-center items-center h-full w-full bg-white border border-custom-300 dark:border-custom-700">
          <img class="w-auto lg:h-[450px] h-auto" src="~/assets/img/sample.jpg" alt="img here">
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'sidebar'
});

// fetch 
import { user } from '~/assets/js/userLogged'
import type { FormError, FormErrorEvent, FormSubmitEvent } from '#ui/types'

const links = [{
  label: 'Notifications',
  to: '/client/notifications'
}, {
  label: 'Details'
}];

const motion = [
  {
    label: 'name',
    value: 'walking'
  },
  {
    label: 'percentage',
    value: '60%'
  },
  {
    label: 'level',
    value: 'normal'
  },
]

const timestamp = [
  {
    label: 'date captured',
    value: user.account_created
  },
  {
    label: 'last update',
    value: user.updated_at
  },
]

const statusOptions = [
  {
    value: 'approved',
    label: 'Approved'
  },
  {
    value: 'ignored',
    label: 'Ignored'
  }
];

const state = reactive({
  status: statusOptions[0].value,
})

const validate = (state: any): FormError[] => {
  const errors = []
  if (!state.status) errors.push({ path: 'status', message: 'Required' })
  return errors
}

const loading = ref(false);
const loadIcon = ref('');
const label = ref('Update');

async function onSubmit(event: FormSubmitEvent<any>) {
  // Do something with data
  console.log(event.data)

  loading.value = true;
  loadIcon.value = 'i-lucide-loader-circle';
  label.value = '';

  setTimeout(() => {
    label.value = 'Update';
    loading.value = false;
    navigateTo('#')
  }, 800)
}

async function onError(event: FormErrorEvent) {
  const element = document.getElementById(event.errors[0].id)
  element?.focus()
  element?.scrollIntoView({ behavior: 'smooth', block: 'center' })
}

</script>
