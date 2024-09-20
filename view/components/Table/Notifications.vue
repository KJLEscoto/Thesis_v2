<template>
  <section class="items-center grid gap-5">
    <div class="flex sm:gap-0 gap-5 sm:flex-row flex-col-reverse sm:justify-between justify-center lg:items-end">
      <div class="flex gap-1 justify-start items-center">
        <UInput v-model="q" name="q" placeholder="Search..." icon="i-heroicons-magnifying-glass-20-solid"
          autocomplete="off" color="gray" size="sm"
          :ui="{ rounded: 'rounded', color: { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }, icon: { trailing: { pointer: '' } } }"
          class="w-full sm:w-auto sm:-mb-0 -mb-5">

          <template #trailing>
            <UButton v-show="q !== ''" color="gray" variant="link" icon="i-heroicons-x-mark-20-solid" :padded="false"
              @click="q = ''" class="hover:text-red-400 dark:hover:text-red-600 text-red-700 dark:text-red-400" />
          </template>
        </UInput>
      </div>

      <div class="grid justify-center items-center gap-2">
        <div class="lg:flex justify-end hidden">
          <span class="text-xs leading-5">
            Showing
            <span class="font-medium">{{ startItem }}</span>
            -
            <span class="font-medium">{{ endItem }}</span>
            of
            <span class="font-medium">{{ totalNotifications }}</span>
            results
          </span>
        </div>
        <UPagination :model-value="currentPage" :page-count="pageCount" :total="totalNotifications" :ui="{
          color: 'gray',
          wrapper: 'flex items-center gap-1',
          rounded: '!rounded-full min-w-[30px] justify-center',
          default: {
            activeButton: {
              variant: 'outline'
            }
          }
        }" @update:model-value="updatePage" class="flex justify-center" />
      </div>
    </div>

    <UTable :columns="tableHeaders" :rows="paginatedData" sort-asc-icon="i-heroicons-arrow-up"
      sort-desc-icon="i-heroicons-arrow-down"
      class="max-h-[70vh] max-w-full overflow-auto border rounded border-custom-300 dark:border-custom-800"
      :ui="{ thead: 'sticky top-0 z-10 dark:bg-custom-700 bg-custom-300 cursor-default', tbody: 'bg-custom-100 dark:bg-custom-950 cursor-default' }">

      <template #loading-state>
        <div class="flex items-center justify-center h-32 gap-2">
          <UIcon name="i-lucide-loader-circle" class="animate-spin text-2xl" />
          <p>In a moment...</p>
        </div>
      </template>

      <template #id-data="{ index }">
        <span>
          {{ (currentPage - 1) * pageCount + index + 1 }}
        </span>
      </template>

      <template #action-data="{ row }">
        <UTooltip text="View" :popper="{ arrow: true, placement: 'right' }"
          :ui="{ background: 'dark:bg-custom-800 bg-custom-50', arrow: { background: 'dark:before:bg-custom-700 before:bg-custom-300' } }">
          <UIcon name="i-lucide-eye" class="text-xl hover:opacity-75 text-blue-500" @click="openModal()" />
        </UTooltip>
      </template>
    </UTable>

    <div class="flex justify-center lg:hidden">
      <span class="text-xs leading-5">
        Showing
        <span class="font-medium">{{ startItem }}</span>
        -
        <span class="font-medium">{{ endItem }}</span>
        of
        <span class="font-medium">{{ totalNotifications }}</span>
        results
      </span>
    </div>
  </section>
</template>

<script setup lang="ts">
import { faker } from '@faker-js/faker';
import { ModalViewNotifications } from '#components';

const motions = ['pickpocketing', 'shoplifting', 'stealing', 'burglary', 'grab', 'snatch'];

// Generate mock data for notifications
const generateData = (numRows: number) => {
  return Array.from({ length: numRows }, (_, i) => ({
    id: i + 1,
    date: faker.date.recent().toISOString().split('T')[0],
    motion_detected: faker.helpers.arrayElement(motions),
  }));
};

const notifications = ref(generateData(27));
const currentPage = ref(1);
const pageCount = ref(20);
const q = ref('');

// Table headers configuration
const tableHeaders = [
  { key: 'id', label: '#' },
  { key: 'date', label: 'Date' },
  { key: 'motion_detected', label: 'Motion Detected' },
  { key: 'action', label: 'Action' },
];

// Filter rows based on the search query
const filteredRows = computed(() => {
  return q.value
    ? notifications.value.filter((item) =>
        Object.values(item).some((value) =>
          String(value).toLowerCase().includes(q.value.toLowerCase())
        )
      )
    : notifications.value;
});

// Pagination logic
const totalNotifications = computed(() => filteredRows.value.length);

const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * pageCount.value;
  return filteredRows.value.slice(start, start + pageCount.value);
});

// Update page
const updatePage = (page: number) => {
  currentPage.value = page;
};

// Start and end items for the current page
const startItem = computed(() => (currentPage.value - 1) * pageCount.value + 1);

const endItem = computed(() => {
  const end = currentPage.value * pageCount.value;
  return Math.min(end, totalNotifications.value);
});

// Action for viewing notifications 
const openModal = () => {
  const modal = useModal();
  modal.open(ModalViewNotifications);
};

// Reset pagination when the search query changes
watch(q, () => {
  currentPage.value = 1;
});
</script>
