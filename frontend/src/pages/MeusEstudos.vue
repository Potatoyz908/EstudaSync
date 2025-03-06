<script setup>
import { onMounted, computed } from "vue";
import { useEstudaSyncStore } from "../store/estudasyncStore";
import { useRouter } from "vue-router";

const store = useEstudaSyncStore();
const router = useRouter();

onMounted(() => {
  store.fetchEstudos();
});

const totalTempoEstudado = computed(() => {
  return store.estudos.reduce((total, estudo) => total + estudo.tempo_estudado, 0);
});
</script>

<template>
  <div class="p-6 max-w-4xl mx-auto">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-indigo-800">Meus Estudos</h1>
      <div class="bg-indigo-100 rounded-lg px-4 py-2 text-indigo-800 font-medium">
        Total: {{ totalTempoEstudado }} minutos
      </div>
    </div>

    <div v-if="store.estudos.length > 0" class="mt-4 bg-white rounded-lg shadow-md">
      <ul class="divide-y divide-gray-100">
        <li 
          v-for="estudo in store.estudos" 
          :key="estudo.id" 
          class="p-4 flex justify-between items-center hover:bg-indigo-50 transition-colors duration-150"
        >
          <div class="flex items-center">
            <div class="bg-indigo-600 h-10 w-10 rounded-full flex items-center justify-center text-white mr-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </div>
            <div>
              <h3 class="font-medium text-gray-800">{{ estudo.titulo }}</h3>
              <p class="text-sm text-gray-500">Matéria</p>
            </div>
          </div>
          <div class="flex items-center">
            <div class="bg-green-100 rounded-full px-4 py-1 mr-4">
              <span class="text-green-700 font-medium">{{ estudo.tempo_estudado }} min</span>
            </div>
            <button class="text-gray-500 hover:text-indigo-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
              </svg>
            </button>
          </div>
        </li>
      </ul>
    </div>
    
    <div v-else class="mt-4 bg-white rounded-lg shadow-md p-10 text-center">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto text-gray-300 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
      </svg>
      <p class="text-gray-500 mb-4">Nenhum estudo registrado ainda.</p>
      <button 
        class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg transition-colors duration-150 flex items-center mx-auto"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Adicionar Estudo
      </button>
    </div>

    <div class="mt-6 flex justify-center">
      <button 
        @click="router.push('/home')" 
        class="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2 rounded-lg transition-colors duration-150 flex items-center"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Voltar
      </button>
    </div>
  </div>
</template>