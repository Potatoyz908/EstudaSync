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
  <div class="page-container">
    <div class="container">
      <h1 class="title">📖 Meus Estudos</h1>
      <p class="total">
        ⏳ Total de Estudo: <strong>{{ totalTempoEstudado }} min</strong>
      </p>

      <ul v-if="store.estudos.length" class="estudo-list">
        <li
          v-for="estudo in store.estudos"
          :key="estudo.id"
          class="estudo-item"
        >
          <span class="study-title">🎥 {{ estudo.titulo }}</span>
          <span class="study-time">⏱ {{ estudo.tempo_estudado }} min</span>
        </li>
      </ul>

      <p v-else class="message">⚠️ Nenhum estudo registrado ainda.</p>

      <button @click="router.push('/home')" class="button">Voltar</button>
    </div>
  </div>
</template>

<style scoped>
/* 🔥 Fundo e layout geral */
.page-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(
    135deg,
    #1a1d3a,
    #2c2f5c
  ); /* 🔥 Gradiente bonito */
  padding: 20px;
  overflow-x: hidden;
}

/* 📖 Container principal */
.container {
  max-width: 600px;
  width: 100%;
  background: white;
  text-align: center;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

/* 📌 Título */
.title {
  font-size: 28px;
  color: #333;
  margin-bottom: 15px;
}

/* ⏳ Total de Estudo */
.total {
  background: #6a11cb;
  color: white;
  padding: 10px 15px;
  border-radius: 8px;
  font-size: 18px;
  display: inline-block;
  margin-bottom: 20px;
}

/* 📖 Lista de estudos */
.estudo-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.estudo-item {
  background: #f8f9fa;
  padding: 12px 15px;
  border-radius: 8px;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 16px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.study-title {
  font-weight: bold;
  color: #333;
}

.study-time {
  color: #6a11cb;
  font-weight: bold;
}

/* ⚠️ Mensagem caso não tenha estudos */
.message {
  font-size: 16px;
  color: #ff4d4d;
  background: rgba(255, 77, 77, 0.1);
  padding: 10px;
  border-radius: 8px;
  display: inline-block;
}

/* 🔙 Botão de Voltar */
.button {
  width: 100%;
  max-width: 250px;
  padding: 14px;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}

.button:hover {
  background-color: #5907a5;
}

/* 🔄 Responsividade */
@media (max-width: 600px) {
  .container {
    padding: 20px;
  }

  .title {
    font-size: 24px;
  }

  .estudo-item {
    font-size: 14px;
    padding: 10px;
  }

  .button {
    font-size: 16px;
    padding: 12px;
  }
}
</style>
