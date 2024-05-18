<template>
  <div class="h-auto w-full p-5">
    <header class="lg:flex block justify-between items-center mb-5">
      <h1 class="font-bold cursor-default lg:mb-0 mb-5">History <span class="font-normal text-sm">({{ totalItems }})</span></h1>
      <div class="flex justify-center lg:justify-end items-center">
        <UPagination
        :prev-button="{ icon: 'i-heroicons-arrow-small-left-20-solid', label: 'Prev', color: 'gray' }"
        :next-button="{ icon: 'i-heroicons-arrow-small-right-20-solid', trailing: true, label: 'Next', color: 'gray' }"
        :model-value="currentPage"
        :page-count="pageCount"
        :total="totalItems"
        show-first
        show-last
        @update:model-value="updatePage"
      />
      </div>
    </header>
    <section class="sm:block flex justify-center items-center">
      <div class="max-h-[80vh] sm:max-w-full max-w-[55vh] overflow-auto border rounded border-custom-300 dark:border-custom-800">
        <table class="w-full whitespace-nowrap">
          <!-- Table Header -->
          <thead class="bg-custom-300 dark:bg-custom-900 sticky top-0">
            <tr>
              <th v-for="(header, index) in headers" :key="index" class="py-2 px-4 text-start uppercase font-semibold text-sm">{{ header }}</th>
            </tr>
          </thead>
          <!-- Table Body -->
          <tbody class="bg-custom-50 text-sm">
            <tr v-for="(item, index) in paginatedData" :key="index" class="dark:bg-custom-950 border-b border-custom-300 dark:border-custom-900">
              <td class="p-4">{{ item.id }}</td>
              <td class="p-4">{{ item.date }}</td>
              <td class="p-4">{{ item.motion_detected }}</td>
              <td class="p-4">
                <span :class="{
                  'text-red-500': item.level === 'danger',
                  'text-yellow-500': item.level === 'warning',
                  'text-green-500': item.level === 'normal'
                }">{{ item.level }}</span>
              </td>
              <td class="p-4">
                <UButton icon="i-lucide-eye" size="xs" label="View" class="flex items-center justify-center" @click="viewAction(item)"/>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'client-sidebar'
})

import { ref, computed } from 'vue';
import { faker } from '@faker-js/faker';

const headers = [
  '#',
  'Date',
  'Motion Detected',
  'Level',
  'Action'
];

const theftMotions = [
  'grab',
  'stealing',
  'pickpocketing',
  'shoplifting',
  'burglary',
  'snatch'
];

const levels = [
  'warning',
  'danger',
  'normal'
];

const levelMapping = {
  warning: ['grab', 'snatch'],
  danger: ['stealing', 'burglary'],
  normal: ['pickpocketing', 'shoplifting']
};

const generateData = (numRows) => {
  const data = [];
  for (let i = 1; i <= numRows; i++) {
    const level = faker.helpers.arrayElement(levels);
    const motion = faker.helpers.arrayElement(levelMapping[level]);
    data.push({
      id: i,
      date: faker.date.recent().toISOString().split('T')[0],
      motion_detected: motion,
      level: level
    });
  }
  return data;
};

const data = ref(generateData(150));
const currentPage = ref(1);
const pageCount = ref(20);
const totalItems = computed(() => data.value.length);

// Calculate total pages
const totalPages = computed(() => Math.ceil(totalItems.value / pageCount.value));

// Paginate data based on current page and page size
const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * pageCount.value;
  const end = start + pageCount.value;
  return data.value.slice(start, end);
});

// Update current page when pagination changes
const updatePage = (page) => {
  currentPage.value = page;
};

const viewAction = (item) => {
  console.log('View action for:', item);
};
</script>
