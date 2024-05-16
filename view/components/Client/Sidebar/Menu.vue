<script setup>
import {
  ref,
  watch
} from 'vue';
import {
  useRoute
} from 'vue-router';

const route = useRoute();

const items = ref([
  {
    title: 'Monitor',
    path: '/client/monitor',
    icon: 'i-lucide-monitor-play'
  },
  {
    title: 'Notifications',
    path: '/client/notifications',
    icon: 'i-lucide-bell'
  },
  {
    title: 'Settings',
    icon: 'mage:settings'
  },
  {
    title: 'Test',
    icon: 'cbi:speedtest'
  },
  {
    title: 'Monitor',
    path: '/client/monitor',
    icon: 'i-lucide-monitor-play'
  },
  {
    title: 'Notifications',
    path: '/client/notifications',
    icon: 'i-lucide-bell'
  },
  {
    title: 'Settings',
    icon: 'mage:settings'
  },
  {
    title: 'Test',
    icon: 'cbi:speedtest'
  },
  {
    title: 'Monitor',
    path: '/client/monitor',
    icon: 'i-lucide-monitor-play'
  },
  {
    title: 'Notifications',
    path: '/client/notifications',
    icon: 'i-lucide-bell'
  },
  {
    title: 'Settings',
    icon: 'mage:settings'
  },
  {
    title: 'Test',
    icon: 'cbi:speedtest'
  },
  {
    title: 'Monitor',
    path: '/client/monitor',
    icon: 'i-lucide-monitor-play'
  },
  {
    title: 'Notifications',
    path: '/client/notifications',
    icon: 'i-lucide-bell'
  },
  {
    title: 'Settings',
    icon: 'mage:settings'
  },
  {
    title: 'Test',
    icon: 'cbi:speedtest'
  },
]);

const activeItem = ref(items.value.find(item => route.path.startsWith(item.path)));

watch(route, () => {
  activeItem.value = items.value.find(item => route.path.startsWith(item.path));
});
</script>

<template>
<div class="lg:w-[250px] w-full tracking-wide">
  <header class="p-5 text-xl border-custom-500 border-b flex lg:gap-0 gap-3 items-center lg:justify-between justify-start">
    <label class="font-semibold">Client</label>
    <ToggleDarkMode class="block" :popper="{ placement: 'right', arrow: true }"/>
  </header>
  <section class="grow overflow-y-auto lg:max-h-[79vh] max-h-[30vh] w-auto">
    <div class="grid gap-2 w-full p-5">
      <nuxt-link :to="item.path" v-for="(item, index) in items" :key="index" class="flex gap-2 items-center px-5 dark:hover:bg-custom-600 hover:bg-custom-200 py-2 transition cursor-pointer rounded-sm relative"  :class="[activeItem === item ? 'bg-custom-400 dark:bg-custom-700' : '']">
        <UIcon :name="item.icon"/>
        <label>{{ item.title }}</label>
      </nuxt-link>
    </div>
  </section>
</div>
</template>
