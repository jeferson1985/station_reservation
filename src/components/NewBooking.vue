<template>
  <div
    class="flex flex-wrap justify-around items-start bg-white w-full h-full rounded-lg p-10"
  >
    <div class="w-full md:w-96 xl:w-5/12 h-fit rounded-xl p-6 bg-purple-600">
      <h1 class="text-xl text-white">Calendario</h1>
      <div class="flex gap-4 float-right mb-2"></div>
      <form action="">
        <label for="" class="text-white">Digite seu nome</label>
        <input
          v-model="user"
          type="number"
          class="w-full border border-solid border-gray-300 rounded-lg px-2 py-2 outline-none mb-4"
        />
        <label for="" class="text-white">Data e Hora de ínicio</label>
        <input
          v-model="start_time"
          type="datetime-local"
          class="w-full border border-solid border-gray-300 rounded-lg px-2 py-2 outline-none mb-4"
        />
        <label for="" class="text-white">Data e Hora de fim</label>
        <input
          v-model="end_time"
          type="datetime-local"
          class="w-full border border-solid border-gray-300 rounded-lg px-2 py-2 outline-none mb-4"
        />
        <label for="room" class="text-white">Sala</label>
        <input
          v-model="room"
          class="w-full border border-solid border-gray-300 rounded-lg px-2 py-2 outline-none mb-4"
          type="text"
        />
        <!-- <select
          v-model="room"
          name=""
          id=""
          class="w-full border border-solid border-gray-300 rounded-lg px-2 py-2 outline-none mb-4"
        >
          <option value="">Selecione uma sala</option>
          <option v-for="item in rooms_list" :key="item.id" :value="item.name">
            {{item.name}}
          </option>
        </select> -->
        <div
          class="flex justify-center text-lg font-bold text-white w-full rounded-lg px-2 py-4 bg-purple-400 hover:bg-purple-900 cursor-pointer"
        >
          <button @click.prevent="sendBooking">Reservar</button>
        </div>
      </form>
    </div>
    <div class="flex flex-col items-center flex-wrap">
      <label for="" class="text-xl font-bold text-gray-400 mb-8">Salas</label>
      <div class="flex flex-wrap justify-center items-center gap-24 w-96">
        <div
          v-for="item in rooms_list"
          :key="item.id"
          class="flex flex-wrap justify-center items-center relative w-14 h-14 rounded-full bg-purple-400"
        >
          <h1 class="text-white">{{ item.id }}</h1>
          <span class="absolute top-14 text-center">{{ item.name }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { title } from "../store/title.js";
import { addMessage } from "../store/alert.js";
import api from "../services/api.js";

export default {
  name: "NewBooking",
  data: () => ({
    date: {
      id: "",
      start_time: "",
      end_time: "",
      user: "",
      room: [],
      name: "",
      rooms_list: [],
      isDark: false,
      start: new Date(),
      end: new Date(),
    },
  }),
  mounted() {
    title.value = "Faça sua reserva";
    this.getRooms();
  },
  computed: {
    formatDate() {
      return moment(this.date.start && this.date.end).format("DD/MM/YYYY");
    },
  },
  methods: {
    async getRooms() {
      try {
        const token = document.cockie;
        const response = await api.get("api/v1/rooms/", {
          headers: {
            "X-CSRFToken": token,
            "Content-Type": "application/x-www-form-urlencoded",
          },
        });
        const data = response.data.map((item) => ({
          id: item.id,
          name: item.name,
        }));
        this.rooms_list = data;
        
        console.log("list rooms", this.rooms_list);
      } catch (error) {
        console.log('error', error.detail)
      }
    },
    async sendBooking() {
      try {
        const token = document.cockie;
        const response = await api.post(
          "api/v1/roomreservation/",
          {
            start_time: this.start_time,
            end_time: this.end_time,
            user: this.user,
            room: this.room,
          },
          {
            headers: {
              "X-CSRFToken": token,
              "Content-Type": "application/x-www-form-urlencoded",
            },
          }
        );
        addMessage("success", "Reserva realizada com sucesso!");
        console.log("post", response);
      } catch (error) {
        addMessage("error", "Erro ao reservar sala!");
      }
    },
  },
};
</script>
