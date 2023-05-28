<template>
  <div
    class="flex flex-col bg-purple-600 w-24 h-auto pt-8"
  >
    <div class="flex justify-center mb-4">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-8 h-8 text-white"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
        />
      </svg>
    </div>
    <div class="flex flex-col">
      <slot name="links" />
    </div>
    <slot name="card" />
  </div>
</template>

<script>
import { show_sidebar, toggle_sidebar } from "../store/title.js";
export default {
  name: "SideBar",
  props: {
    imgSrc: { type: String, required: true },
  },
  computed: {
    showSidebar() {
      return show_sidebar.value;
    },
  },
  methods: {
    dismissSidebar() {
      toggle_sidebar("dismiss");
    },
  },
};
</script>
