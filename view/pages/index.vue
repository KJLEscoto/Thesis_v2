<template>
  <div class="gradient-bg h-full w-full">
    <div class="lg:grid-cols-2 grid-cols-1 lg:grid flex flex-col-reverse lg:h-screen h-auto w-auto lg:gap-20 gap-10 lg:p-20 p-16">
      <section class="m-auto">
        <h1 class="font-bold cursor-default lg:text-4xl text-3xl lg:text-start text-center">Empower Your Security</h1>
        <p class="mt-5 cursor-default lg:text-start text-justify">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut laudantium aliquam beatae. Debitis accusamus aperiam odio repudiandae ea quaerat illo facilis fugiat nobis? Possimus temporibus, sed unde placeat consectetur quae?
          A, ut consequatur. Debitis iste repudiandae explicabo sit nemo natus molestiae optio neque aperiam, itaque cum illo vel quae incidunt quis deleniti ad earum provident quibusdam. Nobis odit consequuntur sint.</p>
        <div class="flex lg:justify-start justify-center mt-7">
          <UButton :loading="false" icon="i-lucide-cctv" label="Start Monitoring" to="/login/as-client" class="px-12 py-4 rounded-full" />
        </div>
      </section>
      <section class="m-auto">
        <img src="/assets/img/cctv-animate.gif" alt="cctv" class="shadow-md lg:scale-125 scale-100 border-8 rounded-full border-custom-500 dark:border-custom-300">
      </section>
    </div>
  </div>
</template>
  