<template>
  <div class="h-auto w-full relative">
    <ToggleDarkMode class="fixed lg:top-20 z-50 top-5 left-5 lg:left-20 duration-200"/>
    <div class="lg:grid-cols-2 grid-cols-1 lg:grid flex flex-col-reverse lg:h-screen h-auto w-auto lg:gap-20 gap-10 lg:p-20 p-16">
      <section class="m-auto">
        <h1 class="font-bold cursor-default lg:text-4xl text-3xl lg:text-start text-center">Empower Your Security</h1>
        <p class="mt-5 cursor-default lg:text-start text-justify">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut laudantium aliquam beatae. Debitis accusamus aperiam odio repudiandae ea quaerat illo facilis fugiat nobis? Possimus temporibus, sed unde placeat consectetur quae?
          A, ut consequatur. Debitis iste repudiandae explicabo sit nemo natus molestiae optio neque aperiam, itaque cum illo vel quae incidunt quis deleniti ad earum provident quibusdam. Nobis odit consequuntur sint.</p>
        <div class="flex lg:justify-start justify-center mt-7">
          <UButton 
            :loading="loading" 
            icon="i-lucide-cctv" 
            label="Start Monitoring" 
            class="px-12 py-4 rounded-full dark:text-custom-100 dark:bg-custom-500 hover:dark:bg-custom-600" 
            @click="handleClick" 
            :loading-icon="loadIcon" />
        </div>
      </section>
      <section class="m-auto">
        <img 
          src="/assets/img/cctv-animate.gif" 
          alt="cctv"
          class="shadow-md lg:scale-125 scale-100 border-8 rounded-full border-custom-500 dark:border-custom-300" >
      </section>
    </div>
  </div>

</template>

<script setup>

const loading = ref(false);
const loadIcon = ref('')

const handleClick = () => {
  loading.value = true;
  loadIcon.value = 'i-lucide-loader-circle'
  setTimeout(() => {
    navigateTo('/login/client');
    loading.value = false;
  }, 800);
};

</script>
  