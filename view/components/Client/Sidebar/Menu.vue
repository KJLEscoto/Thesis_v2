<script setup>
import {
  ref,
  watch
} from 'vue';
import {
  useRoute
} from 'vue-router';

const route = useRoute();

const items = ref([{
    title: 'Monitor',
    path: '/client/monitor'
  },
  {
    title: 'Notifications',
    path: '/client/notifications'
  },
  {
    title: 'Settings',
  },
  {
    title: 'Test',
  },
]);

const activeItem = ref(items.value.find(item => route.path.startsWith(item.path)));

watch(route, () => {
  activeItem.value = items.value.find(item => route.path.startsWith(item.path));
});

</script>

<template>
  <div class="lg:w-[250px] w-full">
    <header class="border-custom-500 border-b p-5 flex justify-between">
      <label class="font-bold text-xl">Client</label>
      <ToggleDarkMode :popper="{ placement: 'right', arrow: true }"/>
    </header>
    <section class="grow overflow-y-auto lg:max-h-[79vh] max-h-[30vh] w-auto p-5">
      <div class="grid gap-2 w-full">
        <nuxt-link :to="item.path" v-for="(item, index) in items" :key="index" class="flex items-center px-5 dark:hover:bg-custom-400 hover:bg-custom-200 py-2 transition cursor-pointer round relative rounded" :class="[activeItem === item ? 'bg-custom-400 dark:bg-custom-600' : '']">
          <p>{{ item.title }}</p>
        </nuxt-link>
      </div>
    </section>
  </div>
</template>