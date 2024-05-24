<template>
  <div>
    <UModal v-model="isOpen" :ui="{background: 'bg-custom-50 dark:bg-custom-900'}" prevent-close>
      <div class="p-4">

        <UForm class="h-auto flex flex-col gap-3" :state="state">

          <header class="flex justify-between">
            <div class="font-semibold cursor-default flex items-center gap-1">
              <UIcon name="i-lucide-user-round-plus" class="text-lg"/>
              <h1 class="font-bold text-lg">New User</h1>
            </div>
            <UIcon name="i-lucide-x" @click="isOpen = false" class="text-red-400 hover:text-red-600 text-xl cursor-pointer"/>
          </header>

          <hr class="border-custom-300 dark:border-custom-500">

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
              <URadioGroup v-model="selectedGender" :options="genderOptions" class="ml-2"/>
            </UFormGroup>

            <UFormGroup class="grid col-span-3" label="Role">
              <UInputMenu :ui="{background: 'bg-white dark:bg-white', rounded: 'rounded', padding: 'p-5'}" v-model="selectedRole" :options="roleOptions" placeholder="Select a role"/>
            </UFormGroup>

            <UFormGroup class="grid col-span-2" label="Status">
              <URadioGroup v-model="selectedStatus" :options="statusOptions" class="ml-2" :ui="{legend: 'font-thin'}"
              />
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

            <UFormGroup class="grid col-span-5" label="Username">
              <UInput type="text" color="gray" size="sm" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
            </UFormGroup>

            <UFormGroup class="grid col-span-5" label="Password">
              <UInput type="password" color="gray" size="sm" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
            </UFormGroup>
          </section>

          <hr class="border-custom-300 dark:border-custom-500">

          <UButton label="Save" class="flex justify-center items-center w-full rounded" type="submit"/>

        </UForm>
      </div>
    </UModal>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const state = reactive({
  first_name: 'kent',
  gender: undefined,
  email: undefined,
  password: undefined
});

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  }
});

const selectedGender = ref('');
const selectedRole = ref('');
const selectedStatus = ref('Active');

const roleOptions = ['Admin', 'Client'];
const statusOptions = ['Active', 'Inactive'];

const genderOptions = [
  { label: 'Male', value: 'male' },
  { label: 'Female', value: 'female' }
];

const emit = defineEmits(['update:modelValue']);
const isOpen = ref(props.modelValue);

watch(() => props.modelValue, (newVal) => {
  isOpen.value = newVal;
});

watch(isOpen, (newVal) => {
  emit('update:modelValue', newVal);
});

</script>