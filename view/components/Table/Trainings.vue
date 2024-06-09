<template>
  <section class="items-center grid gap-5">
    <div class="lg:flex hidden justify-between items-end -mb-3">
      <div class="block">
        <UButton 
          label="Go Train" 
          icon="i-lucide-hand" 
          class="dark:text-custom-200 bg-custom-400 hover:bg-custom-500 dark:bg-custom-700 dark:hover:bg-custom-800 rounded p-2" 
          to="/admin/motion-feed/train"
          size="xs" />
      </div>
      <div class="flex justify-end">
        <span class="text-xs leading-5">
          Showing
          <span class="font-medium">{{ startItem }}</span>
          -
          <span class="font-medium">{{ endItem }}</span>
          of
          <span class="font-medium">{{ totalTrains }}</span>
          results
        </span>
      </div>
    </div>
    <div class="flex sm:gap-0 gap-5 sm:flex-row flex-col-reverse sm:justify-between justify-center">
      <div class="flex gap-1 justify-start items-end">
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
        :total="totalTrains"
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

      <template #level-data="{ row }">
        <UKbd 
          :class="{
            ' bg-green-600 dark:border dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default': row.level === 'normal',
            ' bg-yellow-500 dark:border dark:border-yellow-500 text-custom-100 dark:text-yellow-400 cursor-default': row.level === 'warning',
            'bg-red-600 dark:border dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default': row.level === 'danger',
          }" 
          :value="row.level" />
      </template>

      <template #action-data="{ row }">
        <div class="flex justify-start gap-2">
          <UTooltip 
            text="View" 
            :popper="{ arrow: true, placement: 'bottom' }" 
            :ui="{ background: 'dark:bg-custom-800 bg-custom-50', arrow: { background: 'dark:before:bg-custom-700 before:bg-custom-300'}}" >
            <UIcon 
              name="i-lucide-eye" 
              class="text-xl hover:opacity-50 text-blue-500" 
              @click="viewAction(row)" />
          </UTooltip>
          <UTooltip 
            text="Delete" 
            :popper="{ arrow: true, placement: 'bottom' }" 
            :ui="{ background: 'dark:bg-custom-800 bg-custom-50', arrow: { background: 'dark:before:bg-custom-700 before:bg-custom-300'}}" >
            <UIcon 
              name="i-lucide-trash-2" 
              class="text-xl hover:opacity-50 text-red-500" 
              @click="deleteAction(row)" />
          </UTooltip>
        </div>
      </template>

    </UTable>

    <div class="flex justify-center lg:hidden">
      <span class="text-xs leading-5">
        Showing
        <span class="font-medium">{{ startItem }}</span>
        -
        <span class="font-medium">{{ endItem }}</span>
        of
        <span class="font-medium">{{ totalTrains }}</span>
        results
      </span>
    </div>

  </section>
</template>

<script setup>

// imports
import { ref, computed, watch } from 'vue';
import { faker } from '@faker-js/faker';
import { user } from '~/assets/js/userSample';

// variable to fetch the specific user
const selectedTrain = ref(null);

const levelMapping = {
  normal: ['pickpocketing', 'shoplifting'],
  danger: ['stealing', 'burglary'],
  warning: ['grab', 'snatch'],
};

// fake data
const generateData = (numRows) => {
  const data = [];
  for (let i = 1; i <= numRows; i++) {
    const level = faker.helpers.arrayElement(Object.keys(levelMapping));
    const motion = faker.helpers.arrayElement(levelMapping[level]);

    data.push({
      id: i,
      motion: motion,
      threshold: faker.number.int({ min: 0, max: 100 }) + '%',
      level: level,
      date: faker.date.past().toISOString().split('T')[0], // Date in YYYY-MM-DD format
      action: faker.hacker.verb()
    });
  }
  return data;
};


// variables
const trains = ref(generateData(200));
const currentPage = ref(1);
const pageCount = ref(20);
const q = ref('');


// headers in table
const tableHeaders = [
  { key: 'id', label: `# (${trains.value.length})` },
  { key: 'motion', label: 'Motion', sortable: true }, // grab, reach, snatch, etc.
  { key: 'threshold', label: 'Threshold' }, // percentage to trigger the motion
  { key: 'level', label: 'Level' }, // normal, warning, danger
  { key: 'date', label: 'Date', sortable: true },
  { key: 'action', label: 'Action' }
];


// filter the table in search
const filteredRows = computed(() => {
  if (!q.value) {
    return trains.value;
  }

  return trains.value.filter((person) => {
    return Object.values(person).some((value) => {
      return String(value).toLowerCase().includes(q.value.toLowerCase());
    });
  });
});


// count overall no. of users
const totalTrains = computed(() => filteredRows.value.length);


// pages
const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * pageCount.value;
  const end = start + pageCount.value;
  return filteredRows.value.slice(start, end);
});

const viewAction = (item) => {
  console.log('View action for:', item);
};

const deleteAction = (item) => {
  console.log('Delete action for:', item);
};

const updatePage = (page) => {
  currentPage.value = page;
};

// showing pages
const startItem = computed(() => {
  return (currentPage.value - 1) * pageCount.value + 1;
});

const endItem = computed(() => {
  const end = currentPage.value * pageCount.value;
  return end > totalTrains.value ? totalTrains.value : end;
});


// change status
const toggleStatus = (client) => {
  client.status = client.status === 'Active' ? 'Inactive' : 'Active';
};

const isAdmin = user.role === 'admin';


// Watch the search query and reset the current page to 1 when it changes
watch(q, () => {
  currentPage.value = 1;
});
</script>
