<template>
  <div class="h-full w-full">
    <div class="border-2 border-custom-500 lg:h-full h-[90%] w-full bg-custom-50 dark:bg-custom-200 rounded">
        <section 
          v-show="!camera" 
          class="flex items-center justify-center h-full w-full" >
          <div class="text-red-800 grid justify-center">
            <UIcon 
              class="w-auto h-10 m-auto" 
              name="i-lucide-video-off"  />
              <p class="text-xs tracking-wider font-bold">No Camera Detected.
                <nuxt-link 
                  to="/client/settings" 
                  class="text-blue-900 underline hover:text-white transition-colors duration-150" >
                  Go setup
                </nuxt-link>
              </p>
          </div>
        </section>
        <section 
          v-show="camera" 
          class="flex items-center justify-center h-full w-full" >
            <canvas ref="canvas" class="w-full h-full"></canvas>
        </section>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';

const camera = ref(false)

// Define props
const props = defineProps({
  videoUrl: {
    type: String,
    required: true,
  },
});

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
</script>

<style scoped>
canvas {
  display: block;
}
</style>
