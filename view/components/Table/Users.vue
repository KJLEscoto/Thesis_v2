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
        :total="totalClients"
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
            'border bg-green-600 border-green-600 dark:border-green-700 text-custom-100 dark:text-green-400 cursor-default': row.status === 'Active',
            'border bg-red-600 border-red-600 dark:border-red-700 text-custom-100 dark:text-red-400 cursor-default': row.status === 'Inactive'
          }" 
          :value="row.status" />
      </template>

      <template #actions-data="{ row }">
        <UDropdown 
          mode="hover" 
          :items="actions(row)" 
          :popper="{ placement: 'bottom-end', arrow: 'true', offsetDistance: -10 }" 
          :ui="{ background: 'dark:bg-custom-950 bg-white', item: {disabled: 'cursor-default opacity-100 font-semibold'}}" >
          <UIcon 
            name="i-lucide-ellipsis" 
            class="text-xl" />
        </UDropdown>
      </template>
    </UTable>

  </section>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { faker } from '@faker-js/faker';

const selectedClient = ref(null);

const genderOptions = ['Male', 'Female'];
const roleOptions = ['Client', 'Admin'];
const statusOptions = ['Active', 'Inactive'];

const generateData = (numRows) => {
  const data = [];
  for (let i = 1; i <= numRows; i++) {
    const firstname = faker.person.firstName();
    const lastname = faker.person.lastName();
    const middle_initial = faker.random.alpha().toUpperCase();
    const name = `${firstname} ${middle_initial}. ${lastname}`;

    data.push({
      id: i,
      firstname: firstname,
      lastname: lastname,
      middle_initial: middle_initial,
      gender: faker.helpers.arrayElement(genderOptions),
      username: faker.internet.userName(),
      phone: faker.phone.number('09#########'),
      role: faker.helpers.arrayElement(roleOptions),
      status: faker.helpers.arrayElement(statusOptions),
      name: name 
    });
  }
  return data;
};

const clients = ref(generateData(200));
const currentPage = ref(1);
const pageCount = ref(20);
const q = ref('');

const tableHeaders = [
  { key: 'id', label: `# (${clients.value.length})` },
  { key: 'name', label: 'Name', sortable: true },
  { key: 'username', label: 'Username', sortable: true },
  { key: 'role', label: 'Role', sortable: true },
  { key: 'status', label: 'Status', sortable: true },
  { key: 'actions', label: 'Actions' }
];

const filteredRows = computed(() => {
  if (!q.value) {
    return clients.value;
  }

  return clients.value.filter((person) => {
    return Object.values(person).some((value) => {
      return String(value).toLowerCase().includes(q.value.toLowerCase());
    });
  });
});

const totalClients = computed(() => filteredRows.value.length);

const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * pageCount.value;
  const end = start + pageCount.value;
  return filteredRows.value.slice(start, end);
});

const updatePage = (page) => {
  currentPage.value = page;
};

const toggleStatus = (client) => {
  client.status = client.status === 'Active' ? 'Inactive' : 'Active';
};

const actions = (client) => [
  [{ label: `${client.name}`, disabled: true }],
  [
    {
      label: 'View Details',
      icon: 'i-lucide-eye',
      click: () => {
        selectedClient.value = client;
        navigateTo(`/admin/users/read/${client.id}`);
      }
    },
    {
      label: 'Edit Information',
      icon: 'i-lucide-edit',
      click: () => {
        selectedClient.value = client;
        navigateTo(`/admin/users/update/${client.id}`);
      }
    },
    {
      label: `Status: ${client.status}`,
      icon: 'i-lucide-toggle-left',
      click: () => {
        toggleStatus(client);
      }
    }
  ],
  [
    {
      label: 'Delete Client',
      icon: 'i-lucide-trash-2'
    }
  ]
];

// Watch the search query and reset the current page to 1 when it changes
watch(q, () => {
  currentPage.value = 1;
});
</script>
