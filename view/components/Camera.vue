<template>
  <div class="h-full w-full">
    <div class="border-2 border-custom-500 lg:h-full h-[90%] w-full bg-custom-50 dark:bg-custom-200 rounded">
      <section 
        v-show="!camera" 
        class="flex items-center justify-center h-full w-full">
        <div class="text-red-800 grid justify-center">
          <UIcon 
            class="w-auto h-10 m-auto" 
            name="i-lucide-video-off" />
          <p class="text-xs tracking-wider font-bold">
            No Camera Detected.
            <nuxt-link 
              to="#" 
              class="text-blue-900 underline hover:text-custom-300 transition-colors duration-150">
              Go setup
            </nuxt-link>
          </p>
        </div>
      </section>
      <section 
        v-show="camera" 
        class="flex items-center justify-center h-full w-full bg-custom-400 dark:bg-black relative rounded-sm">

        <div class="flex justify-between absolute top-0 w-full items-center">
          <section class="dark:text-white text-custom-900 w-auto h-auto bg-custom-300 rounded-ss-sm rounded-br-sm px-2 text-sm bg-opacity-50">
            <h1 class="text-lg font-semibold">{{ currentDate }}</h1>
            <p class="">{{ currentTime }}</p>
          </section>
          <section class="px-3" v-if="isLive">
            <UKbd class="flex justify-start gap-1 items-center bg-red-600 px-2 dark:border dark:border-red-700 text-white dark:text-red-400 cursor-default">
              <UIcon name="i-lucide-radio" class="text-base"/>
              <p>LIVE</p>
            </UKbd>
          </section>
        </div>
        
        <canvas ref="canvas" class="w-full h-full"></canvas>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';

// for camera
const camera = ref(true);

// Define props
const props = defineProps({
  videoUrl: {
    type: String,
    required: true,
  },
  isLive: {
    type: Boolean,
    default: true
  }
});

// for video
const canvas = ref(null);

const drawVideoOnCanvas = (video) => {
  const ctx = canvas.value.getContext('2d');

  const drawFrame = () => {
    ctx.drawImage(video, 0, 0, canvas.value.width, canvas.value.height);
    requestAnimationFrame(drawFrame);
  };

  drawFrame();
};

const setupVideo = () => {
  const video = document.createElement('video');
  video.src = props.videoUrl;
  video.crossOrigin = 'anonymous';
  video.autoplay = true;
  video.muted = true;
  video.play();

  video.addEventListener('canplay', () => {
    canvas.value.width = video.videoWidth;
    canvas.value.height = video.videoHeight;
    drawVideoOnCanvas(video);
  });
};

onMounted(() => {
  setupVideo();
});

watch(() => props.videoUrl, () => {
  setupVideo();
});

// For date and time
const currentDate = ref('');
const currentTime = ref('');

const updateDateTime = () => {
  const now = new Date();
  currentDate.value = now.toLocaleDateString();
  currentTime.value = now.toLocaleTimeString();
};

onMounted(() => {
  updateDateTime();
  setInterval(updateDateTime, 1000); // Update every second
});
</script>

<style scoped>
canvas {
  display: block;
}
</style>
