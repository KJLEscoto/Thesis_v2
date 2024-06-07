<template>
  <Settings />
</template>

<script setup>

import { user } from '~/assets/js/userSample';

const initial = computed(() => user.name.charAt(0).toUpperCase());

definePageMeta({
  layout: 'sidebar'
})


</script>