<script lang="ts" setup>
// Columns
const columns = [{
  key: 'id',
  label: '#',
  sortable: false
}, {
  key: 'date',
  label: 'Date',
  sortable: true
}, {
  key: 'motion_detected',
  label: 'Motion Detected',
  sortable: false
}, {
  key: 'level',
  label: 'Level',
  sortable: false
}, {
  key: 'status',
  label: 'Status',
  sortable: false
}, {
  key: 'action',
  label: 'Action',
  sortable: false
}]

// const columns = [{
//   key: 'id',
//   label: '#',
//   sortable: true
// }, {
//   key: 'title',
//   label: 'Title',
//   sortable: true
// }, {
//   key: 'titles',
//   label: 'Title',
//   sortable: true
// }, {
//   key: 'completed',
//   label: 'Completed',
//   sortable: true
// }, {
//   key: 'action',
//   label: 'Action',
//   sortable: false
// }]

const selectedColumns = ref(columns)
const columnsTable = computed(() => columns.filter((column) => selectedColumns.value.includes(column)))

// Selected Rows
const selectedRows = ref([])

function select (row) {
  const index = selectedRows.value.findIndex((item) => item.id === row.id)
  if (index === -1) {
    selectedRows.value.push(row)
  } else {
    selectedRows.value.splice(index, 1)
  }
}

// Mark as
const mark = [
  [{
    key: 'approved',
    label: 'Approved',
    icon: 'i-lucide-badge-check'
  }], [{
    key: 'ignored',
    label: 'Ignored',
    icon: 'i-lucide-badge-minus'
  }]
]

// Filters
const status = [{
  key: 'approved',
  label: 'Approved',
  value: false
}, {
  key: 'ignored',
  label: 'Ignored',
  value: true
}]

// const status = [{
//   key: 'uncompleted',
//   label: 'In Progress',
//   value: false
// }, {
//   key: 'completed',
//   label: 'Completed',
//   value: true
// }]

const search = ref('')
const selectedStatus = ref([])
const searchStatus = computed(() => {
  if (selectedStatus.value?.length === 0) {
    return ''
  }

  if (selectedStatus?.value?.length > 1) {
    return `?completed=${selectedStatus.value[0].value}&completed=${selectedStatus.value[1].value}`
  }

  return `?completed=${selectedStatus.value[0].value}`
})

const resetFilters = () => {
  search.value = ''
  selectedStatus.value = []
}

// Pagination
const sort = ref({ column: 'id', direction: 'asc' as const })
const page = ref(1)
const pageCount = ref(20)
const pageTotal = ref(150) // This value should be dynamic coming from the API
const pageFrom = computed(() => (page.value - 1) * pageCount.value + 1)
const pageTo = computed(() => Math.min(page.value * pageCount.value, pageTotal.value))

// Data
const { data: todos, pending } = await useLazyAsyncData<{
  // data to be retrieve (refer to columns)
  id: number
  date: Date
  motion_detected: string
  level: string
  status: string
  
  // title: string
  // completed: string

}[]>('todos', () => ($fetch as any)(`https://jsonplaceholder.typicode.com/todos${searchStatus.value}`, { // change api to ours
  query: {
    q: search.value,
    '_page': page.value,
    '_limit': pageCount.value,
    '_sort': sort.value.column,
    '_order': sort.value.direction
  }
}), {
  default: () => [],
  watch: [page, search, searchStatus, pageCount, sort]
})

watch(search, () => {
  page.value = 1;
});

const viewAction = (item) => {
  console.log('View action for:', item);
};
</script>

<template>
  
  <div class="flex flex-col gap-5">
    <!-- Filters -->
    <section class="flex items-center gap-3 justify-start">
      <UInput 
        v-model="search" 
        placeholder="Search..." 
        icon="i-heroicons-magnifying-glass-20-solid"
        autocomplete="off"
        color="gray" 
        size="sm" 
        :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}, icon: { trailing: {pointer: '' }}}"
        class="w-full sm:w-auto" >

        <template #trailing>
          <UButton
            v-show="search !== ''"
            color="gray"
            variant="link"
            icon="i-heroicons-x-mark-20-solid"
            :padded="false"
            @click="search = ''"
            class="hover:text-red-400 dark:hover:text-red-600 text-red-700 dark:text-red-400" />
        </template>
      </UInput>
      <UButton
        icon="i-lucide-filter"
        color="gray"
        size="xs"
        :disabled="search === '' && selectedStatus.length === 0"
        @click="resetFilters" >
        Reset
      </UButton>
    </section>

    <!-- Header and Action buttons -->

    
    <section class="flex flex-col bg-custom-50 dark:bg-custom-800 rounded">
      <div class="flex justify-between items-center w-full p-3">
        <div class="flex items-center gap-1.5">
          <span class="text-sm leading-5">Rows per page:</span>
          <USelect
            v-model="pageCount"
            :options="[5, 10, 20, 30, 40]"
            class="w-20"
            size="xs" />
        </div>

        <div class="flex gap-1.5 items-center">
          <UDropdown v-if="selectedRows.length > 0" :items="mark" :ui="{ width: 'w-36' }">
            <UButton
              icon="i-heroicons-chevron-down"
              trailing
              size="xs"
              class="rounded"
            >
              Mark as
            </UButton>
          </UDropdown>

          <USelectMenu v-model="selectedStatus" :options="status" multiple placeholder="Status" class="w-40" />

          <!-- <USelectMenu v-model="selectedColumns" :options="columns" multiple>
            <UButton
              icon="i-heroicons-view-columns"
              color="gray"
              size="xs"
            >
              Columns
            </UButton>
          </USelectMenu> -->
        </div>
      </div>

      <!-- Table -->
      <UTable
        v-model="selectedRows"
        v-model:sort="sort"
        :rows="todos"
        :columns="columnsTable"
        @select="select"
        :loading="pending"
        sort-asc-icon="i-heroicons-arrow-up"
        sort-desc-icon="i-heroicons-arrow-down"
        sort-mode="manual"
        class="max-h-[60vh] max-w-full overflow-auto border dark:border-custom-800 border-custom-300" 
        :ui="{thead: 'sticky top-0 z-10 dark:bg-custom-700 bg-custom-200 cursor-default', tbody: 'bg-custom-100 dark:bg-custom-950'}" >

        <template #loading-state>
          <div class="flex items-center justify-center h-32 gap-2">
            <UIcon name="i-lucide-loader-circle" class="animate-spin text-2xl"/>
            <p>In a moment...</p>
          </div>
        </template>

        <template #id-data="{ index }">
          <span>
            {{ pageFrom + index }}
          </span>
        </template>

        <template #completed-data="{ row }">
          <UBadge size="xs" :label="row.completed ? 'Completed' : 'In Progress'" :color="row.completed ? 'emerald' : 'orange'" variant="subtle" />
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

      <!-- Number of rows & Pagination -->
      <section class="">
        <div class="sm:flex grid sm:justify-between items-center p-3">
          <div class="mb-3 sm:mb-0 flex justify-start">
            <span class="text-xs">
              Showing
              <span class="font-medium">{{ pageFrom }}</span>
              -
              <span class="font-medium">{{ pageTo }}</span>
              of
              <span class="font-medium">{{ pageTotal }}</span>
              results
            </span>
          </div>

          <div class="flex justify-center">
            <UPagination
              v-model="page"
              :page-count="pageCount"
              :total="pageTotal"
              :ui="{
                color: 'red',
                wrapper: 'flex items-center gap-1',
                rounded: '!rounded-full min-w-[32px] justify-center',
                default: {
                  activeButton: {
                    variant: 'outline'
                  }
                }
              }" />
          </div>
        </div>
      </section>
      
    </section>

  </div>
</template>