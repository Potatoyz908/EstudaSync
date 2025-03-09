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
    <h1>📖 Meus Estudos</h1>
    <p class="total">⏳ Total: {{ totalTempoEstudado }} minutos</p>

    <!-- Botão para alternar entre ver apenas os próprios estudos ou todos -->
    <button @click="store.alternarFiltroEstudos" class="toggle-button">
      {{
        store.mostrarTodosEstudos
          ? "👤 Mostrar Apenas Meus Estudos"
          : "🌍 Mostrar Todos os Estudos"
      }}
    </button>

    <ul v-if="store.estudos.length" class="estudo-list">
      <li v-for="estudo in store.estudos" :key="estudo.id" class="estudo-item">
        <span class="titulo">📚 {{ estudo.titulo }}</span> - ⏱️
        {{ estudo.tempo_estudado }} min
      </li>
    </ul>
    <p v-else class="message">⚠️ Nenhum estudo registrado ainda.</p>

    <button @click="router.push('/home')" class="button">🏠 Voltar</button>
  </div>
</template>

<style scoped>
/* 🌟 Estilização da Caixa Principal */
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
  padding: 20px;
  background: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* 🎯 Estilização do Total */
.total {
  background: #6a11cb;
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  font-weight: bold;
}

/* 🔄 Botão de Alternância */
.toggle-button {
  background-color: #6a11cb;
  color: white;
  padding: 12px 22px;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  margin: 15px 0;
  font-weight: bold;
  transition: all 0.3s ease-in-out;
  transform: scale(1);
}

/* 🚀 Animação ao passar o mouse */
.toggle-button:hover {
  background-color: #5907a5;
  transform: scale(1.05);
}

/* ⏬ Efeito ao clicar */
.toggle-button:active {
  transform: scale(0.95);
}

/* 📚 Lista de Estudos */
.estudo-list {
  list-style: none;
  padding: 0;
}

.estudo-item {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 🏷️ Estilo do Título */
.titulo {
  font-weight: bold;
}

/* 🔘 Botão de Voltar */
.button {
  width: 50%;
  padding: 14px;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 25px;
  font-size: 16px;
  margin-top: 20px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s ease-in-out;
  transform: scale(1);
}

/* 🚀 Animação ao passar o mouse */
.button:hover {
  background-color: #5907a5;
  transform: scale(1.05);
}

/* ⏬ Efeito ao clicar */
.button:active {
  transform: scale(0.95);
}
</style>
