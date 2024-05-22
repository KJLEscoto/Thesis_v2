<template>
  <div>
    <UModal v-model="isOpen" :ui="{background: 'dark:bg-custom-900'}" prevent-close>
      <div class="p-4">
        <UForm class="h-auto flex flex-col gap-2" :state="state">
          <header class="flex justify-between">
            <div class="font-semibold cursor-default flex items-center gap-1">
              <UIcon name="i-lucide-user-round-plus" class="text-base"/>
              <p>New User</p>
            </div>
            <UIcon name="i-lucide-x" @click="isOpen = false" class="text-red-400 hover:text-red-600 text-xl cursor-pointer"/>
          </header>
          <hr class="border-custom-300 dark:border-custom-700">
          <section class="grid grid-cols-5 gap-x-3 gap-y-2">
            <section class="col-span-2">
              <label for="first_name">First name</label>
              <input name="first_name" id="first_name"
              class="w-full bg-custom-50 px-1 py-1 text-sm rounded border-2 border-custom-200 transition-all duration-300 outline-none focus:border-custom-700 dark:focus:border-custom-50 mt-1 text-custom-900"/>
            </section>
            <section class="col-span-2">
              <label for="last_name">Last name</label>
              <input name="last_name" id="last_name"
              class="w-full bg-custom-50 px-1 py-1 text-sm rounded border-2 border-custom-200 transition-all duration-300 outline-none focus:border-custom-700 dark:focus:border-custom-50 mt-1 text-custom-900"/>
            </section>
            <section class="col-span-1">
              <label for="middle_initial">M. I.</label>
              <input name="middle_initial" id="middle_initial"
              class="w-full bg-custom-50 px-1 py-1 text-sm rounded border-2 border-custom-200 transition-all duration-300 outline-none focus:border-custom-700 dark:focus:border-custom-50 mt-1 text-custom-900"/>
            </section>
            <section class="col-span-1">
              <label>Gender</label>
              <URadioGroup v-model="selectedGender" :options="genderOptions" class="ml-2"/>
            </section>
          </section>
        </UForm>
      </div>
    </UModal>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const state = reactive({
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