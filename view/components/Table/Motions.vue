<template>
  <section class="items-center grid gap-5">
    <div class="hidden justify-end lg:flex -mb-3">
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
          :ui="{ 
            rounded: 'rounded', 
            color: { gray: { outline: 'dark:bg-custom-100 dark:text-custom-900' } }, 
            icon: { trailing: { pointer: '' } } 
          }"
          class="w-full sm:w-auto sm:-mb-0 -mb-5">

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
        :model-value="currentPage" 
        :page-count="pageCount" 
        :total="totalTrains" 
        :ui="{
          color: 'gray',
          wrapper: 'flex items-center gap-1',
          rounded: '!rounded-full min-w-[30px] justify-center',
          default: {
            activeButton: {
              variant: 'outline'
            }
          }
        }" 
        @update:model-value="updatePage" 
        class="flex justify-center" />
    </div>

    <UTable 
      :columns="tableHeaders" 
      :rows="paginatedData" 
      sort-asc-icon="i-heroicons-arrow-up"
      sort-desc-icon="i-heroicons-arrow-down"
      class="max-h-[70vh] max-w-full overflow-auto border rounded border-custom-300 dark:border-custom-800"
      :ui="{ 
        thead: 'sticky top-0 z-10 dark:bg-custom-700 bg-custom-300 cursor-default', 
        tbody: 'bg-custom-100 dark:bg-custom-950' 
      }">

      <template #id-data="{ index }">
        <span>
          {{ (currentPage - 1) * pageCount + index + 1 }}
        </span>
      </template>

      <!-- <template #level-data="{ row }">
        <UKbd :class="{
          ' bg-green-600 dark:border dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default px-2': row.level === 'normal',
          ' bg-yellow-500 dark:border dark:border-yellow-500 text-custom-100 dark:text-yellow-400 cursor-default px-2': row.level === 'warning',
          'bg-red-600 dark:border dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default px-2': row.level === 'danger',
        }" :value="row.level" />
      </template> -->

      <template #action-data="{ row }">
        <div class="flex justify-start gap-2">

          <UTooltip 
            text="View" 
            :popper="{ 
              arrow: true, 
              placement: 'bottom' 
            }"
            :ui="{ 
              background: 'dark:bg-custom-800 bg-custom-50', 
              arrow: { background: 'dark:before:bg-custom-700 before:bg-custom-300' } 
            }">

            <UIcon 
              name="i-lucide-eye" 
              class="text-xl hover:opacity-50 text-blue-500" 
              @click="viewAction(row)" />
          </UTooltip>

          <UTooltip 
            text="Delete" 
            :popper="{ 
              arrow: true, 
              placement: 'bottom' 
            }"
            :ui="{ 
              background: 'dark:bg-custom-800 bg-custom-50', 
              arrow: { background: 'dark:before:bg-custom-700 before:bg-custom-300' } 
            }">

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
import { ModalViewMotions } from '#components'
import { faker } from '@faker-js/faker';
import { name, playSound } from '~/assets/js/sound'

// variable to fetch the specific user
const selectedTrain = ref(null);

const levelMapping = {
  normal: ['pickpocketing', 'shoplifting'],
  danger: ['stealing', 'burglary'],
  warning: ['grab', 'snatch'],
};

// fake data
const generateData = (numRows) => {
  const train = [];
  for (let i = 1; i <= numRows; i++) {
    const level = faker.helpers.arrayElement(Object.keys(levelMapping));
    const motion = faker.helpers.arrayElement(levelMapping[level]);

    train.push({
      id: i,
      motion: motion,
      threshold: faker.number.int({ min: 0, max: 100 }) + '%',
      level: level,
      date: faker.date.past().toISOString().split('T')[0], // Date in YYYY-MM-DD format
      action: faker.hacker.verb()
    });
  }
  return train;
};


// variables
const trains = ref(generateData(200));
const currentPage = ref(1);
const pageCount = ref(20);
const q = ref('');


// headers in table
const tableHeaders = [
  { key: 'id', label: '#' },
  { key: 'motion', label: 'Motion'}, // grab, reach, snatch, etc.
  { key: 'threshold', label: 'Threshold' }, // percentage to trigger the motion
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
  const modal = useModal()
  modal.open(ModalViewMotions)
};

const toast = useToast()
name.value = 'success_1'

const deleteAction = (item) => {
  if (confirm("Delete this motion?") == true) {

    console.log(item)

    playSound()

    toast.add({
      title: 'Motion Deleted Successfully!',
      icon: 'i-lucide-trash-2',
      timeout: 2500,
      ui: {
        background : 'dark:bg-green-700 bg-green-300', 
        progress: {
          background: 'dark:bg-white bg-green-700 rounded-full'
        }, 
        ring: 'ring-1 ring-green-700 dark:ring-custom-900',
        default: {
          closeButton: { 
            color: 'white',
          }
        },
        icon: 'text-custom-900'
      },
    })
  } else {
    console.log('Cancelled.')
  }
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


// Watch the search query and reset the current page to 1 when it changes
watch(q, () => {
  currentPage.value = 1;
});
</script>
