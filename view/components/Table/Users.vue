<template>
  <section class="sm:block grid justify-center items-center">
    <!-- <div class="max-h-[80vh] sm:max-w-full max-w-[55vh] overflow-auto border rounded border-custom-300 dark:border-custom-800">
      <table class="w-full whitespace-nowrap cursor-default">

        <thead class="bg-custom-300 dark:bg-custom-900 sticky top-0 z-10">
          <tr>
            <th v-for="(header, index) in tableHeaders" :key="index" class="py-2 px-4 text-start uppercase font-semibold text-sm">{{ header }}</th>
          </tr>
        </thead>

        <tbody class="bg-custom-50 text-sm">
          <tr v-for="(client, index) in clients" :key="index" 
              :class="{'dark:bg-custom-700 bg-custom-200': selectedRow === client.id}" 
              class="dark:bg-custom-950 border-b border-custom-300 dark:border-custom-900"
              @click="selectRow(client.id, $event)">
            <td class="p-4">{{ client.id }}</td>
            <td class="p-4">{{ client.name }}</td>
            <td class="p-4">{{ client.username }}</td>
            <td class="p-4">{{ client.role }}</td>
            <td class="p-4">
              <span :class="['inline-block w-3 h-3 rounded-full', client.status === statusOptions[0] ? 'bg-green-500' : 'bg-red-500']"></span>
            </td>
            <td class="p-4">
              <UDropdown mode="hover" :items="actions(client)" :popper="{ placement: 'bottom-end', arrow: 'true', offsetDistance: -10 }" :ui="{ background: 'dark:bg-custom-950 bg-white', item: {disabled: 'cursor-default opacity-100 font-semibold'}}">
                <UIcon name="i-lucide-ellipsis" class="text-xl"/>
              </UDropdown>
            </td>
          </tr>
        </tbody>
      </table>
    </div> -->

    <div class="mb-5 flex sm:flex-row flex-col-reverse gap-5 sm:justify-between justify-center">

      <UInput 
        v-model="q" 
        name="q"
        placeholder="Search..." 
        icon="i-heroicons-magnifying-glass-20-solid"
        autocomplete="off"
        color="gray" 
        size="sm" 
        :ui="{rounded: 'rounded',color: {gray: {outline: 'dark:bg-custom-100 dark:text-custom-900'}}, icon: { trailing: {pointer: '' }}}"
      >

        <template #trailing>
          <UButton
            v-show="q !== ''"
            color="gray"
            variant="link"
            icon="i-heroicons-x-mark-20-solid"
            :padded="false"
            @click="q = ''"
            class="hover:text-red-400 dark:hover:text-red-600 text-red-700 dark:text-red-400"
          />
        </template>
      </UInput>

      <UPagination />

    </div>

    <UTable 
      :columns="tableHeaders" 
      :rows="filteredRows" 
      class="max-h-[80vh] sm:max-w-full max-w-[55vh] overflow-auto border rounded border-custom-300 dark:border-custom-800" 
      :ui="{thead: 'sticky top-0 z-10 dark:bg-custom-700 bg-custom-300 cursor-default', tbody: 'bg-custom-100 dark:bg-custom-950'}"
    >
    
      <template #status-data="{ row }">
        <UKbd 
          :class="{
            'border bg-green-100 border-green-500 text-green-500 dark:text-green-400 cursor-default': row.status === 'Active',
            'border bg-red-100 border-red-500 text-red-500 dark:text-red-400 cursor-default': row.status === 'Inactive'
          }" 
          :value="row.status
        "/>
      </template>

      <template #actions-data="{ row }">
        <UDropdown 
          mode="hover" 
          :items="actions(row)" 
          :popper="{ placement: 'bottom-end', arrow: 'true', offsetDistance: -10 }" 
          :ui="{ background: 'dark:bg-custom-950 bg-white', item: {disabled: 'cursor-default opacity-100 font-semibold'}}"
        >
          <UIcon 
            name="i-lucide-ellipsis" 
            class="text-xl"
          />
        </UDropdown>
      </template>
    </UTable>

    <ModalUserClientView 
      v-model="openView" 
      :clientData="selectedClient"
    />

    <ModalUserClientEdit 
      v-model="openEdit" 
      :clientData="selectedClient"
    />

  </section>

</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { faker } from '@faker-js/faker';

const openView = ref(false);
const openEdit = ref(false);
const selectedClient = ref(null);

const tableHeaders = [{
  key: 'id',
  label: '#'
}, {
  key: 'name',
  label: 'Name',
  sortable: true
}, {
  key: 'username',
  label: 'Username',
  sortable: true
}, {
  key: 'role',
  label: 'Role',
  sortable: true
}, {
  key: 'status',
  label: 'Status',
  sortable: true
}, {
  key: 'actions',
  label: 'Actions'
}
];

const genderOptions = ['Male', 'Female'];
const roleOptions = ['Client', 'Admin']
const statusOptions = ['Active', 'Inactive']

const generateData = (numRows) => {
  const data = [];
  for (let i = 1; i <= numRows; i++) {
    data.push({
      id: i,
      name: faker.person.fullName(),
      gender: faker.helpers.arrayElement(genderOptions),
      username: faker.internet.userName(),
      phone: faker.phone.number('09#########'), // Philippines phone number format
      role: faker.helpers.arrayElement(roleOptions),
      status: faker.helpers.arrayElement(statusOptions)
    });
  }
  return data;
};

const clients = ref(generateData(15));

const toggleStatus = (client) => {
  client.status = client.status === 'Active' ? 'Inactive' : 'Active' || client.status === 'Inactive' ? 'Active' : 'Inactive';
};

const q = ref('')

const filteredRows = computed(() => {
  if (!q.value) {
    return clients.value
  }

  return clients.value.filter((person) => {
    return Object.values(person).some((value) => {
      return String(value).toLowerCase().includes(q.value.toLowerCase())
    })
  })
})

const actions = (client) => [
  [{
    label: `${client.name}`,
    disabled: true
  }],
  [{
    label: 'View Details',
    icon: 'i-lucide-eye',
    click: () => {
      selectedClient.value = client;
      openView.value = true;
    }
  },
  {
    label: 'Edit Information',
    icon: 'i-lucide-edit',
    click: () => {
      selectedClient.value = client;
      openEdit.value = true;
    }
  },
  {
    label: 'Status: ' + client.status,
    icon: 'i-lucide-toggle-left',
    click: () => {
      toggleStatus(client);
    }
  }],
  [{
    label: 'Delete Client',
    icon: 'i-lucide-trash-2'
  }]
];
</script>
