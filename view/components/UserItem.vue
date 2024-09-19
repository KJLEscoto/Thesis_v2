<script setup>
import { ref, computed } from 'vue';
import { user } from '~/assets/js/userLogged';

const initial = computed(() => user.name.charAt(0).toUpperCase());

const isOpen = ref(true)
const router = useRouter();

const logout = () => {
  router.push('/auth');
};

const viewProfile = () => {
  if (user.role === 'client') {
    router.push('/client/settings');
  } else if (user.role === 'admin' || user.role === 'superadmin') {
    router.push('/admin/settings');
  }
};


const items = [
  [{
    label: 'View Profile',
    icon: 'i-lucide-circle-user-round',
    click: viewProfile
  },
  {
    label: 'Logout',
    icon: 'i-lucide-log-out',
    click: logout
  }],
]


</script>

<template>
<div class="m-2 w-auto h-auto">
  <UDropdown 
    v-model="isOpen" 
    :items="items" 
    :popper="{ placement: 'right', arrow: 'true', offsetDistance: 10 }" 
    :ui="{background: 'dark:bg-custom-950', width: 'w-auto', arrow: {background: 'dark:before:bg-custom-400'}}" 
    class="w-full border rounded-sm border-custom-600 lg:block hidden" >
      <div class="w-auto flex justify-start items-center gap-2 p-4" >
        <div class="rounded-full bg-custom-400 dark:bg-custom-500 h-10 w-10 flex justify-center items-center">
          <p class="font-bold text-2xl m-auto">{{ initial }}</p>
        </div>
        <div class="border-l border-custom-400 pl-2 w-auto">
          <p class="tracking-wide lg:truncate lg:max-w-[150px] max-w-full capitalize">{{ user.name }}</p>
          <p class="text-custom-500 dark:text-custom-400 font-semibold text-sm tracking-wider">{{ user.role }}</p>
        </div>
      </div>
  </UDropdown>
  <div class="w-full border rounded-sm border-custom-600 flex justify-between lg:hidden">
    <div class="w-auto flex justify-start items-center gap-2 p-4 cursor-pointer" 
      @click="viewProfile">
      <div class="rounded-full bg-custom-400 dark:bg-custom-500 h-10 w-10 flex justify-center items-center">
        <p class="font-bold text-2xl m-auto">{{ initial }}</p>
      </div>
      <div class="border-l border-custom-400 pl-2 w-auto">
        <p class="tracking-wide lg:truncate lg:max-w-[150px] max-w-full capitalize">{{ user.name }}</p>
        <p class="text-custom-500 dark:text-custom-400 font-semibold text-sm tracking-wider">{{ user.role }}</p>
      </div>
    </div>
    <UButton 
      class="bg-red-500 dark:bg-red-500 hover:bg-red-600 h-10 mr-5 my-auto dark:hover:bg-red-400 text-white dark:text-white rounded" 
      label="Logout" 
      icon="i-lucide-log-out"
      @click="logout" />
  </div>
</div>
</template>
