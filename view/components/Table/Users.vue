<template>
  <section class="items-center grid gap-5">
    <div class="lg:flex hidden justify-between items-end -mb-3">
      <div class="block">

        <UButton 
          label="Add User" 
          icon="i-lucide-user-round-plus"
          class="dark:text-custom-200 bg-custom-400 hover:bg-custom-500 dark:bg-custom-700 dark:hover:bg-custom-800 rounded p-2"
          to="/admin/users/create" 
          size="xs" />
      </div>
      <div class="flex justify-end">
        <span class="text-xs leading-5">
          Showing
          <span class="font-medium">{{ startItem }}</span>
          -
          <span class="font-medium">{{ endItem }}</span>
          of
          <span class="font-medium">{{ totalUsers }}</span>
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

      <div class="grid gap-2">
        <UPagination 
          :model-value="currentPage" 
          :page-count="pageCount" 
          :total="totalUsers" 
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

      <template #status-data="{ row }">
        <UKbd :class="{
          'dark:border bg-green-600 dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default px-2': row.status === 'Active',
          'dark:border bg-red-600 dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default px-2': row.status === 'Inactive'
        }" :value="row.status" />
      </template>

      <template #actions-data="{ row }">

        <UDropdown 
          mode="hover" 
          :items="actions(row)"
          :popper="{ 
            placement: 'bottom-end', 
            arrow: 'true', 
            offsetDistance: -10 
          }"
          :ui="{ 
            background: 'dark:bg-custom-950 bg-white', 
            item: { disabled: 'cursor-disable opacity-100' } 
          }">

          <UIcon 
            name="i-lucide-ellipsis" 
            class="text-xl" />

          <template #item="{ item }">
            <div class="flex justify-between w-full">

              <UTooltip 
                v-if="item.disabled" 
                :text="item.tooltip" 
                :popper="{ placement: 'right-start' }"
                class="flex justify-between w-full">

                <span class="truncate opacity-20">{{ item.label }}</span>

                <UIcon 
                  :name="item.icon" 
                  class="flex-shrink-0 h-4 w-4 text-gray-400 dark:text-gray-500 opacity-20" />
              </UTooltip>

              <div v-else class="flex justify-between w-full">
                <span class="truncate">{{ item.label }}</span>
                <UIcon 
                  :name="item.icon" 
                  class="flex-shrink-0 h-4 w-4 text-gray-400 dark:text-gray-500" />
              </div>
            </div>
          </template>
        </UDropdown>
      </template>

    </UTable>

    <div class="flex justify-center lg:hidden">
      <span class="text-xs leading-5">
        Showing
        <span class="font-medium">{{ startItem }}</span>
        -
        <span class="font-medium">{{ endItem }}</span>
        of
        <span class="font-medium">{{ totalUsers }}</span>
        results
      </span>
    </div>

  </section>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { generateData } from '~/assets/js/users'; // Adjust the path as needed

// Fetch the generated user data
const users = ref(generateData()); // Store the generated data

// Other imports
import { user } from '~/assets/js/userLogged';
import { name, playSound } from '~/assets/js/sound';

// Variables for pagination and search
const currentPage = ref(1);
const pageCount = ref(20);
const q = ref('');

// Table headers
const tableHeaders = [
  { key: 'id', label: '#' },
  { key: 'name', label: 'Name' },
  { key: 'username', label: 'Username' },
  { key: 'role', label: 'Role' },
  { key: 'status', label: 'Status' },
  { key: 'actions', label: 'Actions' }
];

// Filtering rows based on the search query
const filteredRows = computed(() => {
  if (!q.value) {
    return users.value;
  }

  return users.value.filter((person) => {
    return Object.values(person).some((value) => {
      return String(value).toLowerCase().includes(q.value.toLowerCase());
    });
  });
});

// Counting the total number of users
const totalUsers = computed(() => filteredRows.value.length);

// Paginated data
const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * pageCount.value;
  const end = start + pageCount.value;
  return filteredRows.value.slice(start, end);
});

const updatePage = (page) => {
  currentPage.value = page;
};

// Displaying start and end items in pagination
const startItem = computed(() => {
  return (currentPage.value - 1) * pageCount.value + 1;
});

const endItem = computed(() => {
  const end = currentPage.value * pageCount.value;
  return end > totalUsers.value ? totalUsers.value : end;
});

// Toast for status change or delete
const toast = useToast();

// Toggle user status
const toggleStatus = (client) => {
  client.status = client.status === 'Active' ? 'Inactive' : 'Active';
  name.value = 'toggle_1';

  if (client.status === 'Active') {
    toast.add({
      title: 'Status changed: Active!',
      icon: 'i-lucide-toggle-right',
      timeout: 1500,
      ui: {
        background: 'dark:bg-green-700 bg-green-300',
        progress: { background: 'dark:bg-white bg-green-700 rounded-full' },
        ring: 'ring-1 ring-green-700 dark:ring-custom-900',
        default: { closeButton: { color: 'white' } },
        icon: 'text-custom-900',
      },
    });
    playSound();
  } else {
    toast.add({
      title: 'Status changed: Inactive!',
      icon: 'i-lucide-toggle-left',
      timeout: 1500,
      ui: {
        background: 'dark:bg-red-700 bg-red-300',
        progress: { background: 'dark:bg-white bg-red-700 rounded-full' },
        ring: 'ring-1 ring-red-700 dark:ring-custom-900',
        default: { closeButton: { color: 'white' } },
        icon: 'text-custom-900',
      },
    });
    playSound();
  }
};

// Delete user
const deleteAction = (client) => {
  if (confirm('Delete this user?') == true) {
    name.value = 'delete_1';
    toast.add({
      title: 'User Deleted Successfully!',
      icon: 'i-lucide-trash-2',
      timeout: 2000,
      ui: {
        background: 'dark:bg-red-700 bg-red-300',
        progress: { background: 'dark:bg-white bg-red-700 rounded-full' },
        ring: 'ring-1 ring-red-700 dark:ring-custom-900',
        default: { closeButton: { color: 'white' } },
        icon: 'text-custom-900',
      },
    });
    playSound();
  }
};

// Check if user is admin
const isAdmin = user.role === 'admin';

// Actions for each user row
const actions = (client) => [
  [
    {
      title: 'view',
      label: 'View Details',
      icon: 'i-lucide-eye',
      click: () => navigateTo(`/admin/users/${client.username}`),
    },
    {
      title: 'update',
      label: 'Edit Information',
      icon: 'i-lucide-edit',
      click: () => navigateTo(`/admin/users/${client.username}/update`),
      disabled: isAdmin,
      tooltip: isAdmin ? 'Only superadmin can edit' : null,
    },
    {
      title: 'toggle',
      label: `Status: ${client.status}`,
      icon: 'i-lucide-toggle-left',
      click: () => toggleStatus(client),
    },
  ],
  [
    {
      title: 'delete',
      label: 'Delete User',
      icon: 'i-lucide-trash-2',
      disabled: isAdmin,
      tooltip: isAdmin ? 'Only superadmin can delete' : null,
      click: () => deleteAction(client),
    },
  ],
];

// Watch the search query and reset the current page to 1 when it changes
watch(q, () => {
  currentPage.value = 1;
});
</script>
