<template>
  <div>
    <div class="container mx-auto px-4 sm:px-8">
      <div class="py-8">
        <div>
          <h2 class="text-2xl font-bold leading-tight text-gray-400">Reservas</h2>
        </div>
        <div class="-mx-4 sm:-mx-8 px-4 sm:px-8 py-4 overflow-x-auto">
          <div
            class="inline-block min-w-full shadow-md rounded-lg overflow-hidden"
          >
            <table class="min-w-full leading-normal">
              <thead>
                <tr>
                  <th
                    class="px-5 py-3 border-b-2 border-gray-200 bg-purple-600 text-left text-xs font-semibold text-white uppercase tracking-wider"
                  >
                    Nome
                  </th>
                  <th
                    class="px-5 py-3 border-b-2 border-gray-200 bg-purple-600 text-left text-xs font-semibold text-white uppercase tracking-wider"
                  >
                    Estação
                  </th>
                  <th
                    class="px-5 py-3 border-b-2 border-gray-200 bg-purple-600 text-left text-xs font-semibold text-white uppercase tracking-wider"
                  >
                    Data | Hora | Início
                  </th>
                  <th
                    class="px-5 py-3 border-b-2 border-gray-200 bg-purple-600 text-left text-xs font-semibold text-white uppercase tracking-wider"
                  >
                    Data | Hora | Fim
                  </th>
                  <th
                    class="px-5 py-3 border-b-2 border-gray-200 bg-purple-600"
                  ></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in rooms_list" :key="item.id">
                  <td
                    class="px-2 py-5 border-b border-gray-200 bg-white text-sm"
                  >
                    <div class="flex">
                      <div class="ml-3">
                        <p class="text-gray-900 whitespace-no-wrap">
                          {{ item.user }}
                        </p>
                      </div>
                    </div>
                  </td>
                  <td
                    class="px-5 py-5 border-b border-gray-200 bg-white text-sm"
                  >
                    <p class="text-gray-900 whitespace-no-wrap">
                      {{ item.room }}
                    </p>
                  </td>
                  <td
                  class="px-5 py-5 border-b border-gray-200 bg-white text-sm"
                >
                  <span
                    class="relative inline-block px-3 py-1 font-semibold text-green-900 leading-tight"
                  >
                    <span
                      aria-hidden
                      class="absolute inset-0 bg-purple-400 opacity-50 rounded-full"
                    ></span>
                    <span class="relative">{{ item.start_time }}</span>
                  </span>
                </td>
                  <td
                    class="px-5 py-5 border-b border-gray-200 bg-white text-sm"
                  >
                    <span
                      class="relative inline-block px-3 py-1 font-semibold text-green-900 leading-tight"
                    >
                      <span
                        aria-hidden
                        class="absolute inset-0 bg-purple-400 opacity-50 rounded-full"
                      ></span>
                      <span class="relative">{{ item.end_time }}</span>
                    </span>
                  </td>
                  <td
                    class="px-5 py-5 border-b border-gray-200 bg-white text-sm text-right"
                  ></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "./../services/api.js";
import { title } from "../store/title.js";
import moment from "moment";

export default {
  name: "ReservationsList",
  data: () => ({
    rooms_list: [],
    start_time: "",
    end_time: "",
    room: "",
    name: "",
    user: "",
    id: "",
  }),
  mounted() {
    title.value = "Lista de reservas";
    this.getRoomsBooking();
  },
  methods: {
    async getRoomsBooking() {
      try {
        const token = document.cockies;
      const response = await api.get(
        "/api/v1/roomreservation",

        {
          headers: {
            "X-CSRFToken": token,
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      );
      const data = response.data.map((item) => ({
        start_time: this.format_date(item.start_time),
        end_time: this.format_date(item.end_time),
        room: item.room,
        id: item.id,
        user: item.user
      }));
      this.rooms_list = data;
      console.log('success')
      } catch (error) {
        console.log('error', error.detail)
      }
      
    },
    format_date(value) {
      if (value) {
        return moment(String(value)).format("DD/MM/YYYY HH:mm");
      }
    },
  },
};
</script>
