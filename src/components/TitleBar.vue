<template>
    <div class="flex justify-between items-center pt-10 px-3 lg:px-4 pb-5">
      <div class="flex gap-4 items-center">
        <h2 class="text-xl md:text-2xl xl:text-3xl font-bold text-gray-400">{{ title }}</h2>
      </div>
    </div>
  </template>
  
  <script>
  import { title, toggle_sidebar } from '../store/title.js'
  export default {
    name: 'TitleBar',
    components: { },
    data: () => ({}),
    computed: {
      title() {
        return title.value
      },
    },
    methods: {
      toggleSidebar() {
        toggle_sidebar()
      },
    },
  }
  </script>