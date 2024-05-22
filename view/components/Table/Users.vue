<template>
  <div>
    <section class="sm:block flex justify-center items-center">
      <div class="max-h-[80vh] sm:max-w-full max-w-[55vh] overflow-auto border rounded border-custom-300 dark:border-custom-800">
        <table class="w-full whitespace-nowrap cursor-default">
          <!-- Table Header -->
          <thead class="bg-custom-300 dark:bg-custom-900 sticky top-0 z-10">
            <tr>
              <th v-for="(header, index) in tableHeaders" :key="index" class="py-2 px-4 text-start uppercase font-semibold text-sm">{{ header }}</th>
            </tr>
          </thead>
          <!-- Table Body -->
          <tbody class="bg-custom-50 text-sm">
            <tr v-for="(client, index) in clients" :key="index" 
                :class="{'bg-[#d4dfe3] dark:bg-[#24494a]': selectedRow === client.id}" 
                class="dark:bg-custom-950 border-b border-custom-300 dark:border-custom-900"
                @click="selectRow(client.id, $event)">
              <td class="p-4">{{ client.id }}</td>
              <td class="p-4">{{ client.name }}</td>
              <td class="p-4">{{ client.email }}</td>
              <!-- <td class="p-4">{{ client.phone }}</td> -->
              <td class="p-4">{{ client.role }}</td>
              <td class="p-4">
                <span :class="['inline-block w-3 h-3 rounded-full', client.status === 'active' ? 'bg-green-500' : 'bg-red-500']"></span>
              </td>
              <td class="p-4">
                <UDropdown mode="hover" :items="actions(client)" :popper="{ placement: 'bottom-end', arrow: 'true', offsetDistance: -10 }" :ui="{ background: 'dark:bg-custom-950 bg-white', item: {disabled: 'cursor-default opacity-100 font-semibold'}}">
                  <UIcon name="i-lucide-ellipsis" class="text-xl"/>
                </UDropdown>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <ModalUserClientView v-model="openView" :clientData="selectedClient"/>
      <ModalUserClientEdit v-model="openEdit" :clientData="selectedClient"/>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { faker } from '@faker-js/faker';

const openView = ref(false);
const openEdit = ref(false);
const selectedClient = ref(null);

const tableHeaders = [
  'No.',
  'Name',
  'Email',
  'Role',
  'Status',
  'Action'
];

const genderOptions = [
  { label: 'Male', value: 'male' },
  { label: 'Female', value: 'female' }
];

const generateData = (numRows) => {
  const data = [];
  for (let i = 1; i <= numRows; i++) {
    data.push({
      id: i,
      name: faker.person.fullName(),
      gender: faker.helpers.arrayElement(genderOptions).value,
      email: faker.internet.email(),
      phone: faker.phone.number('09#########'), // Philippines phone number format
      role: faker.helpers.arrayElement(['client', 'admin']),
      status: faker.helpers.arrayElement(['active', 'inactive'])
    });
  }
  return data;
};

const clients = ref(generateData(25));
const selectedRow = ref(null);

const selectRow = (id, event) => {
  selectedRow.value = id;
  event.stopPropagation();
};

const toggleStatus = (client) => {
  client.status = client.status === 'active' ? 'inactive' : 'active';
};

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
