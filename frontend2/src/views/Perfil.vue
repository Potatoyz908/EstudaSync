<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import api from "../api";

const route = useRoute();
const usuarioId = route.params.id;

const usuario = ref(null);
const carregando = ref(true);
const erro = ref("");

// Função para buscar os dados do usuário
const carregarPerfil = async () => {
  try {
    const response = await api.get(`/usuarios/${usuarioId}/perfil/`);
    usuario.value = response.data;
  } catch (e) {
    erro.value = "Erro ao carregar perfil do usuário.";
  } finally {
    carregando.value = false;
  }
};

// Chamada da função ao entrar na página
onMounted(() => {
  carregarPerfil();
});
</script>

<template>
  <div class="container">
    <div v-if="carregando" class="loading">Carregando...</div>
    <div v-else-if="erro" class="error">{{ erro }}</div>
    <div v-else class="perfil-card">
      <h1 class="perfil-nome">👤 {{ usuario.nome }}</h1>
      <p class="perfil-info">
        🕒 Tempo Total de Estudo:
        <strong>{{ usuario.tempo_total_estudo }}</strong>
      </p>

      <div class="progresso-container">
        <p>📈 Progresso:</p>
        <div class="progresso-barra">
          <div
            class="progresso-preenchido"
            :style="{ width: usuario.progresso_porcentagem + '%' }"
          ></div>
        </div>
        <p>{{ usuario.progresso_porcentagem }}% concluído</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.loading,
.error {
  font-size: 18px;
  color: red;
  font-weight: bold;
}

.perfil-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.perfil-nome {
  font-size: 24px;
  color: #6a11cb;
}

.perfil-info {
  font-size: 18px;
  margin: 10px 0;
}

.progresso-container {
  margin-top: 20px;
}

.progresso-barra {
  width: 100%;
  height: 20px;
  background: #e0e0e0;
  border-radius: 10px;
  overflow: hidden;
}

.progresso-preenchido {
  height: 100%;
  background: #6a11cb;
  transition: width 0.5s ease-in-out;
}
</style>
