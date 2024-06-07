<template>
  <section class="items-center grid gap-5">
    <div class="flex sm:gap-0 gap-5 sm:flex-row flex-col-reverse sm:justify-between justify-center">
      <div class="flex gap-1 justify-start items-center">
        <div class="lg:block hidden">
          <UButton 
            label="Add User" 
            icon="i-lucide-user-round-plus" 
            class="dark:text-custom-200 bg-custom-400 hover:bg-custom-500 dark:bg-custom-700 dark:hover:bg-custom-800 rounded p-2" 
            to="/admin/users/create"
            size="xs" />
        </div>
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
        :total="totalUsers"
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

      <template #status-data="{ row }">
        <UKbd 
          :class="{
            'dark:border bg-green-600 dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default': row.status === 'Active',
            'dark:border bg-red-600 dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default': row.status === 'Inactive'
          }" 
          :value="row.status" />
      </template>

      <template #actions-data="{ row }">
        <UDropdown 
          mode="hover" 
          :items="actions(row)" 
          :popper="{ placement: 'bottom-end', arrow: 'true', offsetDistance: -10 }" 
          :ui="{ background: 'dark:bg-custom-950 bg-white', item: { disabled: 'cursor-disable opacity-100' } }" >
          
          <UIcon 
            name="i-lucide-ellipsis" 
            class="text-xl" />

          <template #item="{ item }">
            <div class="flex justify-between w-full">
              <UTooltip v-if="item.disabled" :text="item.tooltip" :popper="{ placement: 'right-start' }" class="flex justify-between w-full">
                <span class="truncate opacity-20">{{ item.label }}</span>
                <UIcon :name="item.icon" class="flex-shrink-0 h-4 w-4 text-gray-400 dark:text-gray-500 opacity-20" />
              </UTooltip>
              <div v-else class="flex justify-between w-full">
                <span class="truncate">{{ item.label }}</span>
                <UIcon :name="item.icon" class="flex-shrink-0 h-4 w-4 text-gray-400 dark:text-gray-500" />
              </div>
            </div>
          </template>
        </UDropdown>
      </template>

    </UTable>

  </section>
</template>

<script setup>

// imports
import { ref, computed, watch } from 'vue';
import { faker } from '@faker-js/faker';
import { user } from '~/assets/js/userSample';

// variable to fetch the specific user
const selectedUser = ref(null);


const roleOptions = ['Client', 'Admin'];
const statusOptions = ['Active', 'Inactive'];


// fake data
const generateData = (numRows) => {
  const data = [];
  for (let i = 1; i <= numRows; i++) {
    const firstname = faker.person.firstName();
    const lastname = faker.person.lastName();
    const middle_initial = faker.string.alpha().toUpperCase();
    const name = `${firstname} ${middle_initial}. ${lastname}`;

    data.push({
      id: i,
      username: faker.internet.userName(),
      role: faker.helpers.arrayElement(roleOptions),
      status: faker.helpers.arrayElement(statusOptions),
      name: name 
    });
  }
  return data;
};


// variables
const users = ref(generateData(200));
const currentPage = ref(1);
const pageCount = ref(20);
const q = ref('');


// headers in table
const tableHeaders = [
  { key: 'id', label: `# (${users.value.length})` },
  { key: 'name', label: 'Name', sortable: true },
  { key: 'username', label: 'Username' },
  { key: 'role', label: 'Role', sortable: true },
  { key: 'status', label: 'Status', sortable: true },
  { key: 'actions', label: 'Actions' }
];


// filter the table in search
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


// count overall no. of users
const totalUsers = computed(() => filteredRows.value.length);


// pages
const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * pageCount.value;
  const end = start + pageCount.value;
  return filteredRows.value.slice(start, end);
});

const updatePage = (page) => {
  currentPage.value = page;
};


// change status
const toggleStatus = (client) => {
  client.status = client.status === 'Active' ? 'Inactive' : 'Active';
};

const isAdmin = user.role === 'admin';

// for actions
const actions = (client) => [
  // [{ label: `${client.name}`, disabled: true }],
  [
    {
      title: 'read',
      label: 'View Details',
      icon: 'i-lucide-eye',
      click: () => {
        selectedUser.value = client;
        navigateTo(`/admin/users/read/${client.id}`);
      }
    },
    {
      title: 'update',
      label: 'Edit Information',
      icon: 'i-lucide-edit',
      click: () => {
        selectedUser.value = client;
        navigateTo(`/admin/users/update/${client.id}`);
      },
      disabled: isAdmin,
      tooltip: isAdmin ? 'Only superadmin can edit' : null
    },
    {
      title: 'toggle',
      label: `Status: ${client.status}`,
      icon: 'i-lucide-toggle-left',
      click: () => {
        toggleStatus(client);
      }
    }
  ],
  [
    {
      title: 'delete',
      label: 'Delete Client',
      icon: 'i-lucide-trash-2',
      disabled: isAdmin,
      tooltip: isAdmin ? 'Only superadmin can delete' : null
    }
  ]
];

// Watch the search query and reset the current page to 1 when it changes
watch(q, () => {
  currentPage.value = 1;
});
</script>
