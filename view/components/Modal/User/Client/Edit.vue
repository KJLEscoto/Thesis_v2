<template>
  <UModal v-model="isOpen" :ui="{background: 'dark:bg-custom-900'}" prevent-close>
    <div class="p-4">
      <div v-if="clientData" class="h-60 flex flex-col gap-2">
        <div class="flex justify-between">
          <h1 class="font-semibold cursor-default text-lg">Editable Information</h1>
          <UIcon name="i-lucide-x" @click="isOpen = false" class="text-red-400 hover:text-red-600 text-xl cursor-pointer"/>
        </div>
        <hr class="border-custom-300 dark:border-custom-700">
        <div class="grid grid-cols-4 h-auto overflow-auto gap-y-2 p-1">
          <p class="text-start">Name:</p>
          <div class="col-span-3 text-start">
            <input name="first_name" id="first_name" v-model="clientData.name"
            class="w-full dark:bg-custom-800 bg-custom-300 px-1 py-1 text-sm rounded border-2 dark:border-custom-600 border-custom-400 transition-all duration-300 outline-none focus:border-custom-700 focus:bg-custom-100 dark:focus:border-custom-50 dark:focus:bg-custom-200 dark:focus:text-custom-900 focus:text-custom-900 mt-1 dark:text-custom-300 text-custom-900"/>
          </div>

          <p class="text-start">Gender:</p>
          <div class="col-span-3 text-start dark:font-light">
            <URadioGroup v-model="clientData.gender" :options="genderOptions"/>
          </div>

          <p class="text-start">Email:</p>
          <div class="col-span-3 text-start">
            <input name="first_name" id="first_name" v-model="clientData.email"
            class="w-full dark:bg-custom-800 bg-custom-300 px-1 py-1 text-sm rounded border-2 dark:border-custom-600 border-custom-400 transition-all duration-300 outline-none focus:border-custom-700 focus:bg-custom-100 dark:focus:border-custom-50 dark:focus:bg-custom-200 dark:focus:text-custom-900 focus:text-custom-900 mt-1 dark:text-custom-300 text-custom-900"/>
          </div>

          <p class="text-start">Phone:</p>
          <div class="col-span-3 text-start">
            <input name="phone" id="phone" v-model="clientData.phone"
            class="w-full dark:bg-custom-800 bg-custom-300 px-1 py-1 text-sm rounded border-2 dark:border-custom-600 border-custom-400 transition-all duration-300 outline-none focus:border-custom-700 focus:bg-custom-100 dark:focus:border-custom-50 dark:focus:bg-custom-200 dark:focus:text-custom-900 focus:text-custom-900 mt-1 dark:text-custom-300 text-custom-900"/>
          </div>

        </div>
      </div>
      
      <hr class="border-custom-300 dark:border-custom-700 mt-2 mb-2">
        <UButton label="Update" class="flex justify-center items-center w-full mt-2" @click="updateClientDetails"/>
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

const genderOptions = [
  { label: 'Male', value: 'male' },
  { label: 'Female', value: 'female' }
];

watch(() => props.modelValue, (newVal) => {
  isOpen.value = newVal;
});

watch(isOpen, (newVal) => {
  emit('update:modelValue', newVal);
});

const closeEditModal = () => {
  isOpen.value = false;
  emit('close-edit');
};

const updateClientDetails = () => {
  closeEditModal();
};
</script>
