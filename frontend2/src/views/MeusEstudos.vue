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
  return store.estudos.reduce(
    (total, estudo) => total + estudo.tempo_estudado,
    0
  );
});
</script>

<template>
  <div class="container">
    <h1>Meus Estudos</h1>
    <p class="total">Total: {{ totalTempoEstudado }} minutos</p>

    <ul v-if="store.estudos.length" class="estudo-list">
      <li v-for="estudo in store.estudos" :key="estudo.id" class="estudo-item">
        {{ estudo.titulo }} - {{ estudo.tempo_estudado }} min
      </li>
    </ul>
    <p v-else class="message">Nenhum estudo registrado ainda.</p>

    <button @click="router.push('/home')" class="button">Voltar</button>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
  padding: 20px;
}
.total {
  background: #007bff;
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
}
.estudo-list {
  list-style: none;
  padding: 0;
}
.estudo-item {
  padding: 8px;
  border-bottom: 1px solid #ddd;
}
.button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
}
</style>
