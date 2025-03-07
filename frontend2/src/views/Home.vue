<script setup>
import { ref, onMounted } from "vue";
import { useEstudaSyncStore } from "../store/estudasyncStore";
import { useRouter } from "vue-router";

const store = useEstudaSyncStore();
const router = useRouter();
const nomeUsuario = ref(localStorage.getItem("usuario") || "Usuário");
const titulo = ref("");
const tempo = ref("");
const isLoading = ref(false);
const errorMessage = ref("");

onMounted(() => {
  store.fetchRanking();
});

const registrarEstudo = async () => {
  if (titulo.value && tempo.value > 0) {
    isLoading.value = true;
    try {
      await store.registrarEstudo(titulo.value, parseInt(tempo.value));
      titulo.value = "";
      tempo.value = "";
    } catch (error) {
      errorMessage.value = "Erro ao registrar estudo!";
    }
    isLoading.value = false;
  } else {
    errorMessage.value = "Preencha todos os campos!";
    setTimeout(() => (errorMessage.value = ""), 3000);
  }
};
</script>

<template>
  <div class="container">
    <h1>Bem-vindo, {{ nomeUsuario }}</h1>

    <div class="box">
      <h2>Registrar Estudo</h2>
      <input
        v-model="titulo"
        placeholder="Nome do Vídeo/Material"
        class="input"
      />
      <input
        v-model="tempo"
        type="number"
        placeholder="Tempo (min)"
        class="input"
      />
      <button @click="registrarEstudo" :disabled="isLoading" class="button">
        {{ isLoading ? "Salvando..." : "Registrar" }}
      </button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>

    <div class="box">
      <h2>Ranking</h2>
      <ul v-if="store.ranking.length">
        <li v-for="user in store.ranking" :key="user.id" class="ranking-item">
          {{ user.usuario }} - {{ user.pontos }} pontos
        </li>
      </ul>
      <p v-else class="message">Nenhum ranking disponível.</p>
    </div>

    <button @click="router.push('/meus-estudos')" class="button">
      Meus Estudos
    </button>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
  padding: 20px;
}
.box {
  background: #fff;
  padding: 15px;
  margin-top: 15px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.input {
  width: 100%;
  padding: 8px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.button:disabled {
  background-color: #999;
}
.error {
  color: red;
  font-size: 14px;
}
</style>
