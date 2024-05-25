<template>
  <UModal 
    v-model="isOpen" 
    :ui="{background: 'bg-custom-50 dark:bg-custom-900'}"
  >
    <div class="p-4">
      <div 
        v-if="clientData" 
        class="h-60 flex flex-col gap-2"
      >
        <div class="flex justify-between">
          <div class="flex gap-1 justify-start items-center">
            <UIcon 
              name="i-lucide-book-user" 
              class="text-lg"
            />
            <h1 class="font-semibold cursor-default text-lg">Client Details</h1>
          </div>
          <UButton 
            icon="i-lucide-edit" 
            label="Edit" 
            size="2xs" 
            @click="handleEdit"
          />
        </div>
        <hr class="border-custom-300 dark:border-custom-700">
        <div class="grid grid-cols-4 h-auto overflow-auto gap-1 p-1">
          <p class="text-start">Name:</p>
          <p class=" col-span-3 text-start dark:font-light">{{ clientData.name }}</p>

          <p class="text-start">Gender:</p>
          <p class=" col-span-3 text-start dark:font-light">{{ clientData.gender }}</p>

          <p class="text-start">Username:</p>
          <p class=" col-span-3 text-start dark:font-light">{{ clientData.username }}</p>

          <p class="text-start">Phone:</p>
          <p class=" col-span-3 text-start dark:font-light">{{ clientData.phone }}</p>

          <p class="text-start">Role:</p>
          <p class=" col-span-3 text-start dark:font-light">{{ clientData.role }}</p>

          <p class="text-start">Status:</p>
          <p class=" col-span-3 text-start dark:font-light"> {{ clientData.status }}</p>

          <p class="text-start">Acc. Created:</p>
          <p class=" col-span-3 text-start dark:font-light">date here</p>

          <p class="text-start">Last Update:</p>
          <p class=" col-span-3 text-start dark:font-light">date here</p>
        </div>
      </div>

      <hr class="border-custom-300 dark:border-custom-700 mb-2 mt-2">

      <UButton 
        label="Okay" 
        class="flex justify-center items-center w-full rounded" 
        @click="isOpen = false"
      />

    </div>
  </UModal>

  <ModalUserClientEdit 
    v-model="openEdit" 
    :clientData="clientData" 
    @close-edit="closeEdit"
  />

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

const emit = defineEmits(['update:modelValue']);
const isOpen = ref(props.modelValue);
const openEdit = ref(false);

watch(() => props.modelValue, (newVal) => {
  isOpen.value = newVal;
});

watch(isOpen, (newVal) => {
  emit('update:modelValue', newVal);
});

const handleEdit = () => {
  openEdit.value = true;
  isOpen.value = false;
};

const closeEdit = () => {
  openEdit.value = false;
  isOpen.value = true;
};
</script>
