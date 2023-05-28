<template>
  <div class="flex justify-center bg-white w-full h-screen rounded-lg">
    <img src="https://www.treehugger.com/thmb/my3Rm0OW1WlCTi5iSkipXYghBfg=/1560x1120/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/__opt__aboutcom__coeus__resources__content_migration__treehugger__images__2018__02__groundfloor-c619aef8bb32408eb3cd5d5f2c88ed8f.jpg" alt="" class="relative w-96 md:w-full h-5/6">
  </div>
</template>

<script>
import { title } from "../store/title.js";

export default {
  name: "MapOffice",
  data: () => ({
  }),
  mounted() {
    title.value = "Mapa Escritório";
  },
};
</script>
