<template>
  <header class="lg:flex block justify-between items-center mb-5">
    <h1 class="font-semibold text-lg cursor-default lg:mb-0 mb-5 relative">Saved History <span class="font-normal text-xs absolute">({{ totalItems }})</span></h1>
    <div class="flex justify-center lg:justify-end items-center">
      <UPagination
      :prev-button="{ icon: 'i-heroicons-arrow-small-left-20-solid', label: 'Prev', color: 'gray' }"
      :next-button="{ icon: 'i-heroicons-arrow-small-right-20-solid', trailing: true, label: 'Next', color: 'gray' }"
      :model-value="currentPage"
      :page-count="pageCount"
      :total="totalItems"
      show-first
      show-last
      @update:model-value="updatePage" />
    </div>
  </header>
  
  <UTable 
      :columns="tableHeaders" 
      :rows="paginatedData" 
      class="max-h-[80vh] sm:max-w-full max-w-[55vh] overflow-auto border rounded border-custom-300 dark:border-custom-800" 
      :ui="{thead: 'sticky top-0 z-10 dark:bg-custom-700 bg-custom-300 cursor-default', tbody: 'bg-custom-100 dark:bg-custom-950'}" >
      <template #level-data="{ row }">
        <UKbd 
          :class="{
            'border bg-green-600 border-green-600 dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default': row.level === 'normal',
            'border bg-yellow-500 border-yellow-500 dark:border-yellow-500 text-custom-100 dark:text-yellow-400 cursor-default': row.level === 'warning',
            'border bg-red-600 border-red-600 dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default': row.level === 'danger',
          }" 
          :value="row.level" />
      </template>
      <template #action-data="{ row }">
        <UTooltip 
          text="View" 
          :popper="{ arrow: true, placement: 'right' }" 
          :ui="{ background: 'dark:bg-custom-800 bg-custom-50', arrow: { background: 'dark:before:bg-custom-700 before:bg-custom-300'}}" >
          <UIcon 
            name="i-lucide-eye" 
            class="text-xl hover:opacity-75" 
            @click="viewAction(row)" />
        </UTooltip>
      </template>
    </UTable>
</template>

<script setup>
import { ref, computed } from 'vue';
import { faker } from '@faker-js/faker';

const tableHeaders = [{
  key: 'id',
  label: '#'
}, {
  key: 'date',
  label: 'Date',
  sortable: true
}, {
  key: 'motion_detected',
  label: 'Motion Detected',
  sortable: true
}, {
  key: 'level',
  label: 'Level',
  sortable: true
}, {
  key: 'action',
  label: 'Action'
}
];

const levelMapping = {
  normal: ['pickpocketing', 'shoplifting'],
  danger: ['stealing', 'burglary'],
  warning: ['grab', 'snatch'],
};

const generateData = (numRows) => {
  const data = [];
  for (let i = 1; i <= numRows; i++) {
    const level = faker.helpers.arrayElement(Object.keys(levelMapping));
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

const data = ref(generateData(1500));
const currentPage = ref(1);
const pageCount = ref(20);
const totalItems = computed(() => data.value.length);

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