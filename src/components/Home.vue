<template>
  <div class="bg-gray-100 relative">
    <div class="absolute right-4 md:right-24 top-6">
      <FlashMessages />
    </div>
    <div class="absolute h-1 w-full z-30" :class="[getGradient]" />
    <div class="flex min-h-screen bg-lighter relative">
      <div
        id="drag-overlay"
        on-drop="onDrop"
        class="bg-black-50 bg-opacity-60 w-screen h-full absolute bottom-0 left-0 z-40 hidden"
        @drop="onDrop"
      ></div>
      <SideBar>
        <template #links>
          <div class="flex flex-col items-center space-y-8 mt-12">
            <SidebarLinks
              v-for="(link, index) in links"
              :key="index"
              :icon="link.icon"
              :text="link.text"
              :link="link.to"
            />
          </div>
        </template>
      </SideBar>
      <div class="flex flex-col w-full px-6">
        <TitleBar />
        <div class="h-full">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SideBar from "./SideBar.vue";
import SidebarLinks from "./SideBarLinks.vue";
import TitleBar from "./TitleBar.vue";
import FlashMessages from "./FlashMessages.vue";
import { title } from "../store/title.js";

export default {
  name: "Home",
  components: { SideBar, TitleBar, SidebarLinks, FlashMessages },
  data: () => ({
    count: 0,
    rooms_list: [],
    name: "",
    id: "",
  }),
  mounted() {
    title.value = "Bem Vindo";
    this.$router.push({ name: 'welcome' });
  },
  computed: {
    links() {
      return [
        {
          icon: "calendar",
          text: "Calendário",
          to: "/map",
        },
        {
          icon: "folder",
          text: "Reservas",
          to: "/reservations_list",
        },
        {
          icon: "reservation",
          text: "Faça sua reserva",
          to: "/new_booking",
        },
      ];
    },
  },
  methods: {},
};
</script>
