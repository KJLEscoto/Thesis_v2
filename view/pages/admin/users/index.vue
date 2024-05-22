<template>
  <div class="h-screen w-full p-5">
    
    <header class="font-bold cursor-default mb-5">
      <h1>Users</h1>
    </header>

    <UButton label="Add User" icon="i-lucide-user-round-plus" class="dark:text-custom-200 bg-custom-400 hover:bg-custom-500 dark:bg-custom-700 dark:hover:bg-custom-800" @click="newClientForm" size="xs"/>

    <div class="mt-5">
      <TableUsers />
    </div>

    <ModalFormAdd v-model="newClient"/>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const newClient = ref(false)

const newClientForm = () => {
  newClient.value = true;
}

definePageMeta({
  layout: 'sidebar'
})
</script>
