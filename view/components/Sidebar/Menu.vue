<script setup>
import { ref, computed, watch } from 'vue';
import { useRoute } from 'vue-router';
import { user } from '~/assets/js/userSample';

const route = useRoute();

const clientItems = ref([
  {
    title: 'Monitor',
    path: '/client/monitor',
    icon: 'i-lucide-monitor'
  },
  {
    title: 'Notifications',
    path: '/client/notifications',
    icon: 'i-lucide-bell'
  },
  {
    title: 'Settings',
    path: '/client/settings',
    icon: 'i-lucide-settings-2'
  },
]);

const adminItems = ref([
  {
    title: 'Dashboard',
    path: '/admin/dashboard',
    icon: 'i-lucide-layout-dashboard'
  },
  {
    title: 'Motion Feed',
    path: '/admin/motion-feed',
    icon: 'i-lucide-file-input'
  },
  {
    title: 'List of Users',
    path: '/admin/users',
    icon: 'i-lucide-users-round'
  }, 
  // {
  //   title: 'Notification Log',
  //   path: '/admin/notification-log',
  //   icon: 'i-lucide-book-open-text'
  // },
  {
    title: 'Settings',
    path: '/admin/settings',
    icon: 'i-lucide-settings'
  },
]);

const items = computed(() => {
  return user.role === 'admin' || user.role === 'superadmin' ? adminItems.value : clientItems.value;
});

const activeItem = ref(items.value.find(item => route.path.startsWith(item.path)));

watch([route, items], () => {
  activeItem.value = items.value.find(item => route.path.startsWith(item.path));
});

</script>


<template>
<div class=" w-full tracking-wide">
  <header class="p-5 text-xl border-custom-500 border-b flex lg:gap-0 gap-3 items-center lg:justify-between justify-start ">

    <label class="font-semibold">
      {{
        user.role === 'superadmin' ? 'Superadmin' :
        user.role === 'admin' ? 'Admin' :
        user.role === 'client' ? 'Client' :
        ''
      }}
    </label>

    <ToggleDarkMode 
      class="block" 
      :popper="{ placement: 'right', arrow: true }" />
  </header>
  <section class="grow overflow-y-auto lg:max-h-[79vh] max-h-[30vh] w-auto">
    <div class="grid gap-2 w-full p-5">
      <nuxt-link 
        :to="item.path" 
        v-for="(item, index) in items" 
        :key="index" 
        class="flex gap-2 items-center px-5 dark:hover:bg-custom-600 hover:bg-white py-2 transition cursor-pointer rounded-sm relative" 
        :class="[activeItem === item ? 'bg-custom-200 dark:bg-custom-700' : '']" >
        <UIcon :name="item.icon" class="text-lg"/>
        <label>{{ item.title }}</label>
      </nuxt-link>
    </div>
  </section>
</div>
</template>
