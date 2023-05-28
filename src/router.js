import { createRouter, createWebHistory } from "vue-router";
import ReservationsList from "./components/ReservationsList.vue";
import NewBooking from "./components/NewBooking.vue";
import MapOffice from "./components/MapOffice.vue";
import Home from "./components/Home.vue";
import WelcomePage from "./components/WelcomePage.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,

      children: [
        {
          path: "/welcome",
          name: "welcome",
          component: WelcomePage,
        },
        {
          path: "/reservations_list",
          name: "reservations",
          component: ReservationsList,
        },
        {
          path: "/new_booking",
          name: "new_booking",
          component: NewBooking,
        },
        {
          path: "/map",
          name: "map",
          component: MapOffice,
        },
      ],
    },
  ],
});

export default router;
