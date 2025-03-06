<script setup>
import { ref, onMounted } from "vue";
import { useEstudaSyncStore } from "../store/estudasyncStore";
import { useRouter } from "vue-router";

const store = useEstudaSyncStore();
const router = useRouter();
const nomeUsuario = ref("");

const titulo = ref("");
const tempo = ref("");

onMounted(() => {
  nomeUsuario.value = localStorage.getItem("usuario") || "Usuário";
  store.fetchRanking();
});

const registrarEstudo = () => {
  if (titulo.value && tempo.value > 0) {
    store.registrarEstudo(titulo.value, parseInt(tempo.value));
    titulo.value = "";
    tempo.value = "";
  }
};
</script>

<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold text-center">Bem-vindo, {{ nomeUsuario }}</h1>

    <div class="mt-6 p-4 bg-gray-100 rounded-md">
      <h2 class="text-lg font-semibold">Registrar Estudo</h2>
      <input v-model="titulo" placeholder="Nome do Vídeo/Material"
        class="p-2 border w-full mt-2 rounded">
      <input v-model="tempo" type="number" placeholder="Tempo (min)"
        class="p-2 border w-full mt-2 rounded">
      <button @click="registrarEstudo"
        class="bg-blue-600 text-white px-4 py-2 mt-2 w-full rounded hover:bg-blue-500">
        Registrar
      </button>
    </div>

    <div class="mt-6 p-4 bg-gray-100 rounded-md">
      <h2 class="text-lg font-semibold">Ranking</h2>
      <ul v-if="store.ranking.length" class="mt-2">
        <li v-for="user in store.ranking" :key="user.id" class="p-2 border-b">
          {{ user.usuario }} - {{ user.pontos }} pontos
        </li>
      </ul>
      <p v-else class="text-gray-500">Nenhum ranking disponível.</p>
    </div>

    <div class="mt-6 flex justify-center">
      <button @click="router.push('/meus-estudos')" class="bg-gray-500 text-white px-4 py-2 rounded">
        Meus Estudos
      </button>
    </div>
  </div>
</template>
