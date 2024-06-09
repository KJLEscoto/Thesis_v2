<template>
  <section class="items-center grid gap-5">
  <div class="flex sm:gap-0 gap-5 sm:flex-row flex-col-reverse sm:justify-between justify-center lg:items-end">
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

      <div class="grid justify-center items-center gap-2">
        <div class="lg:flex justify-end hidden">
          <span class="text-xs leading-5">
            Showing
            <span class="font-medium">{{ startItem }}</span>
            -
            <span class="font-medium">{{ endItem }}</span>
            of
            <span class="font-medium">{{ totalData }}</span>
            results
          </span>
        </div>
        <UPagination
          :prev-button="{ icon: 'i-heroicons-arrow-small-left-20-solid', label: 'Prev', color: 'gray' }"
          :next-button="{ icon: 'i-heroicons-arrow-small-right-20-solid', trailing: true, label: 'Next', color: 'gray' }"
          :model-value="currentPage"
          :page-count="pageCount"
          :total="totalData"
          show-first
          show-last
          @update:model-value="updatePage"
          class="flex justify-center" />
      </div>
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
      <UTooltip 
        text="View" 
        :popper="{ arrow: true, placement: 'right' }" 
        :ui="{ background: 'dark:bg-custom-800 bg-custom-50', arrow: { background: 'dark:before:bg-custom-700 before:bg-custom-300'}}" >
        <UIcon 
          name="i-lucide-eye" 
          class="text-xl hover:opacity-75 text-blue-500" 
          @click="viewAction(row)" />
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
      <span class="font-medium">{{ totalData }}</span>
      results
    </span>
  </div>
</section>
</template>

<script setup>
import { ref, computed } from 'vue';
import { faker } from '@faker-js/faker';

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

const data = ref(generateData(30));
const currentPage = ref(1);
const pageCount = ref(20);
const q = ref('');

const tableHeaders = [{
  key: 'id',
  label: '#'
}, {
  key: 'date',
  label: 'Date',
  sortable: true
}, {
  key: 'motion_detected',
  label: 'Motion Detected'
}, {
  key: 'level',
  label: 'Level'
}, {
  key: 'action',
  label: 'Action'
}
];

const filteredRows = computed(() => {
  if (!q.value) {
    return data.value;
  }

  return data.value.filter((person) => {
    return Object.values(person).some((value) => {
      return String(value).toLowerCase().includes(q.value.toLowerCase());
    });
  });
});

const totalData = computed(() => filteredRows.value.length);

const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * pageCount.value;
  const end = start + pageCount.value;
  return filteredRows.value.slice(start, end);
});

const updatePage = (page) => {
  currentPage.value = page;
};

// showing pages
const startItem = computed(() => {
  return (currentPage.value - 1) * pageCount.value + 1;
});

const endItem = computed(() => {
  const end = currentPage.value * pageCount.value;
  return end > totalData.value ? totalData.value : end;
});

const viewAction = (item) => {
  console.log('View action for:', item);
};

watch(q, () => {
  currentPage.value = 1;
});
</script>