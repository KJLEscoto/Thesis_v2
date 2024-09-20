<template>

  <UseHead title="Edit - Settings - Client" />

  <UModal 
    v-model="isOpen" 
    :ui="{background: 'bg-custom-50 dark:bg-custom-900'}" 
    prevent-close
  >
    <div class="p-4">
      <UForm 
        v-if="clientData" 
        class="h-auto flex flex-col gap-3" 
        :state="state"
      >

        <header class="flex justify-between">
          <div class="font-semibold cursor-default flex items-center gap-1">
            <UIcon 
              name="i-lucide-edit" 
              class="text-lg" />
            <h1 class="font-bold text-lg">Editable Information</h1>
          </div>
          <UIcon 
            name="i-lucide-x" 
            @click="closeModal" 
            class="text-red-400 hover:text-red-600 text-xl cursor-pointer" />
        </header>

        <hr class="border-custom-300 dark:border-custom-500">

        <section class="grid grid-cols-5 gap-3">
          <UFormGroup 
            class="grid col-span-2" 
            label="First name" >
            <UInput 
              v-model="clientData.name" 
              type="text" color="gray" 
              size="sm" :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}"  />
          </UFormGroup>

          <UFormGroup 
            class="grid col-span-2" 
            label="Last name" >
            <UInput 
              type="text" 
              color="gray" 
              size="sm" 
              :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
          </UFormGroup>

          <UFormGroup 
            class="grid col-span-1" 
            label="M. I." >
            <UInput 
              type="text" 
              color="gray" 
              size="sm" 
              :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
          </UFormGroup>

          <UFormGroup 
            class="grid col-span-2" 
            label="Gender" >
            <URadioGroup 
              disabled 
              v-model="clientData.gender" 
              :options="genderOptions" 
              class="ml-2" />
          </UFormGroup>

          <UFormGroup 
            class="grid col-span-3" 
            label="Role" >
            <UInputMenu 
              v-model="clientData.role" 
              disabled color="gray" 
              :ui="{rounded: 'rounded', color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" 
              :uiMenu="{background: 'dark:bg-custom-400', option: {color: 'dark:text-white', active: 'dark:bg-custom-600', empty: 'dark:text-white'}, empty: 'dark:text-white'}" 
              :options="roleOptions" 
              placeholder="Select a role" />
          </UFormGroup>

          <UFormGroup 
            class="grid col-span-2" 
            label="Status" >
            <URadioGroup 
              v-model="clientData.status" 
              :options="statusOptions" 
              class="ml-2" 
              :uiRadio="radioGroupUI" />
          </UFormGroup>

          <UFormGroup class="grid col-span-3">
            <template #label>
              <div class="flex items-center justify-start gap-1">
                <p class="text-base">Phone no.</p>
                <UIcon name="i-emojione-v1-flag-for-philippines" />
              </div>
            </template>
            <UInput 
              type="text" 
              color="gray" 
              size="sm" 
              :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
          </UFormGroup>

          <UFormGroup 
            class="grid col-span-5" 
            label="Username" >
            <UInput 
              disabled 
              v-model="clientData.username" 
              type="text" 
              color="gray" 
              size="sm" 
              :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
          </UFormGroup>

          <UFormGroup 
            class="grid col-span-5" 
            label="Password" >
            <UInput 
              type="password" 
              color="gray" 
              size="sm" 
              :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}}" />
          </UFormGroup>
        </section>

        <hr class="border-custom-300 dark:border-custom-500">

        <UButton 
          label="Update" 
          class="flex justify-center items-center w-full rounded" 
          type="submit" 
          @click="updateClientDetails" />

      </UForm>
    </div>
  </UModal>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  },
  clientData: {
    type: Object,
    default: () => ({})
  }
});

const emit = defineEmits(['update:modelValue', 'close-edit']);
const isOpen = ref(props.modelValue);

const selectedStatus = ref('');

const statusOptions = ['Active', 'Inactive'];
const genderOptions = ['Male', 'Female'];

// const radioGroupUI = computed(() => ({
//   color: selectedStatus.value === statusOptions[0] 
//     ? 'text-green-500'
//     : 'text-red-500'
// }));


// watch(() => props.modelValue, (newVal) => {
//   isOpen.value = newVal;
// });

// watch(isOpen, (newVal) => {
//   emit('update:modelValue', newVal);
// });

// const closeEditModal = () => {
//   isOpen.value = false;
//   emit('close-edit');
// };

// const updateClientDetails = () => {
//   closeEditModal();
// };

const modal = useModal()

const closeModal = () => {
  modal.reset()
}

</script>
