<template>
  <section class="items-center grid gap-5">
    <div class="flex sm:gap-0 gap-5 sm:flex-row flex-col-reverse sm:justify-between justify-center">
      <div class="flex gap-1 justify-start items-center">
        <UInput 
          v-model="q" 
          name="q"
          placeholder="Search..." 
          icon="i-heroicons-magnifying-glass-20-solid"
          autocomplete="off"
          color="gray" 
          size="sm" 
          :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}, icon: { trailing: {pointer: '' }}}"
          class="w-full sm:w-auto sm:-mb-0 -mb-5" >

          <template #trailing>
            <UButton
              v-show="q !== ''"
              color="gray"
              variant="link"
              icon="i-heroicons-x-mark-20-solid"
              :padded="false"
              @click="q = ''"
              class="hover:text-red-400 dark:hover:text-red-600 text-red-700 dark:text-red-400" />
          </template>
        </UInput>
      </div>

      <UPagination
        :prev-button="{ icon: 'i-heroicons-arrow-small-left-20-solid', label: 'Prev', color: 'gray' }"
        :next-button="{ icon: 'i-heroicons-arrow-small-right-20-solid', trailing: true, label: 'Next', color: 'gray' }"
        :model-value="currentPage"
        :page-count="pageCount"
        :total="totalLogs"
        show-first
        show-last
        @update:model-value="updatePage"
        class="flex justify-center" />
    </div>

    <UTable 
      :columns="tableHeaders" 
      :rows="paginatedData" 
      class="max-h-[80vh] max-w-full overflow-auto border rounded border-custom-300 dark:border-custom-800" 
      :ui="{thead: 'sticky top-0 z-10 dark:bg-custom-700 bg-custom-300 cursor-default', tbody: 'bg-custom-100 dark:bg-custom-950'}" >

      <template #id-data="{ index }">
        <span>
          {{ (currentPage - 1) * pageCount + index + 1 }}
        </span>
      </template>

      <template #message-data="{ row }">
        <div class="max-w-[30vh] truncate">
          {{ row.message }}
        </div>
      </template>

      <template #status-data="{ row }">
        <UKbd 
          :class="{
            'border bg-green-600 border-green-600 dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default': row.status === 'Active',
            'border bg-red-600 border-red-600 dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default': row.status === 'Inactive'
          }" 
          :value="row.status" />
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

  </section>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { faker } from '@faker-js/faker';

const statusOptions = ['idk', 'idk'];

const motions = {
  normal: ['pickpocketing', 'shoplifting'],
  danger: ['stealing', 'burglary'],
  warning: ['grab', 'snatch'],
};

const getRandomMotion = () => {
  const categories = Object.keys(motions);
  const randomCategory = faker.helpers.arrayElement(categories);
  return faker.helpers.arrayElement(motions[randomCategory]);
};

const generateData = (numRows) => {
  const data = [];
  const fullNames = Array.from({ length: 10 }, () => faker.person.fullName()); // Generate 10 fake full names
  for (let i = 1; i <= numRows; i++) {
    const fullName = fullNames[(i - 1) % 10]; // Repeat full names across pages
    data.push({
      date: faker.date.recent().toLocaleDateString(), // Generate recent date
      motion_detected: getRandomMotion(), // Get random motion detected
      user_name: fullName, // Use generated full name
      message: faker.lorem.sentence(), // Generate a random sentence
      status: faker.helpers.arrayElement(statusOptions) // Generate status
    });
  }
  return data;
};

const logs = ref(generateData(100));
const currentPage = ref(1);
const pageCount = ref(20);
const q = ref('');

const tableHeaders = [
  { key: 'id', label: `# (${logs.value.length})` },
  { key: 'date', label: 'Date', sortable: true },
  { key: 'motion_detected', label: 'Motion Detected' },
  { key: 'user_name', label: 'Detected By' },
  { key: 'message', label: 'Message'},
  { key: 'status', label: 'Status' },
  { key: 'action', label: 'Action' }
];

const filteredRows = computed(() => {
  if (!q.value) {
    return logs.value;
  }

  return logs.value.filter((person) => {
    return Object.values(person).some((value) => {
      return String(value).toLowerCase().includes(q.value.toLowerCase());
    });
  });
});

const totalLogs = computed(() => filteredRows.value.length);

const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * pageCount.value;
  const end = start + pageCount.value;
  return filteredRows.value.slice(start, end);
});

const updatePage = (page) => {
  currentPage.value = page;
};

const viewAction = (row) => {
  console.log('View action for row:', row);
};

// Watch the search query and reset the current page to 1 when it changes
watch(q, () => {
  currentPage.value = 1;
});
</script>
