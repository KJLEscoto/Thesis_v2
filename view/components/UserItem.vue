<script setup>
import { ref, computed } from 'vue';
import { user } from '~/assets/js/userRole';

const capitalizedName = computed(() => {
  const maxLength = 13; // Adjust the maximum length as needed
  const truncatedName = user.name.length > maxLength ? user.name.slice(0, maxLength) + '...' : user.name;
  return truncatedName.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
});

const initial = computed(() => user.name.charAt(0).toUpperCase());

const isOpen = ref(true)
const router = useRouter();

const logout = () => {
  router.push('/login/client');
};

const items = [
  [{
    label: 'Logout',
    icon: 'i-lucide-log-out',
    click: logout
  }]
]


</script>

<template>
<div class="m-2 w-auto h-auto">
  <UDropdown v-model="isOpen" :items="items" :popper="{ placement: 'right', arrow: 'true', offsetDistance: 10 }" :ui="{background: 'dark:bg-custom-800', width: 'w-auto', arrow: {background: 'dark:before:bg-custom-400'}}" class="w-full border rounded-sm border-custom-500">
    <!-- <UTooltip 
      class="w-full flex justify-start items-center gap-2 relative p-4" 
      :ui="{ background: 'dark:bg-custom-800 bg-custom-50', arrow: { background: 'dark:before:bg-custom-950 before:bg-custom-300'}}" 
      :popper="{ placement: 'bottom' , arrow: true }" 
      text="See Profile"
    > -->
      <div class="w-full flex justify-start items-center gap-2 relative p-4" >
        <div class="rounded-full bg-custom-400 h-10 w-10 flex justify-center items-center">
          <p class="font-bold text-2xl m-auto">{{ initial }}</p>
        </div>
        <div class="border-l border-custom-400 pl-2">
          <p class="tracking-wide">{{ capitalizedName }}</p>
          <p class="text-custom-500 dark:text-custom-400 font-semibold text-sm tracking-wider">{{ user.role }}</p>
        </div>
      </div>
      <!-- <UIcon name="i-lucide-chevron-right" class="absolute top-8 right-5 dark:text-custom-500" /> -->
    <!-- </UTooltip> -->
  </UDropdown>
</div>
</template>
