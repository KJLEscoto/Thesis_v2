<template>
  <div class="h-screen w-full p-5 flex flex-col gap-5">
    
    <header class="cursor-default flex justify-between">
      <h1 class="text-xl font-semibold">Users</h1>

      <UButton 
        label="Add User" 
        icon="i-lucide-user-round-plus" 
        class="dark:text-custom-200 bg-custom-400 hover:bg-custom-500 dark:bg-custom-700 dark:hover:bg-custom-800" 
        @click="newClientForm" 
        size="xs"
      />
    </header>

    <TableUsers />

    <ModalFormAdd v-model="newClient"/>
  </div>
</template>

<script setup>

const newClient = ref(false)

const newClientForm = () => {
  newClient.value = true;
}

definePageMeta({
  layout: 'sidebar'
})
</script>
