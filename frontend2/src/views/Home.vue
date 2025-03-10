<script setup>
import { ref, onMounted, watchEffect } from "vue";
import { useEstudaSyncStore } from "../store/estudasyncStore";
import { useRouter } from "vue-router";
import { computed } from "vue";

const store = useEstudaSyncStore();
const router = useRouter();
const nomeUsuario = ref("Usuário");
const mostrarTabelaPontuacao = ref(false); // Estado da tabela de pontuação
const rankingOrdenado = computed(() => {
  return [...store.ranking].sort((a, b) => b.pontos - a.pontos);
});

// 🔥 Variáveis reativas adicionadas corretamente
const titulo = ref("");
const tempo = ref("");
const isLoading = ref(false);
const errorMessage = ref("");
const successMessage = ref("");

// Atualiza os dados ao entrar na página
onMounted(() => {
  nomeUsuario.value = localStorage.getItem("usuario_nome") || "Usuário";
  store.usuarioId = localStorage.getItem("usuario_id");
  store.fetchEstudos();
  store.fetchRanking();
});

// Atualiza o nome do usuário dinamicamente
watchEffect(() => {
  nomeUsuario.value = localStorage.getItem("usuario_nome") || "Usuário";
});

// Função para alternar a exibição da tabela
const toggleTabelaPontuacao = () => {
  mostrarTabelaPontuacao.value = !mostrarTabelaPontuacao.value;
};

// 🔥 FUNÇÃO PARA DEFINIR CLASSE DO RANKING 🔥
const getRankingClass = (index) => {
  if (index === 0) return "gold"; // 1º lugar - Ouro
  if (index === 1) return "silver"; // 2º lugar - Prata
  if (index === 2) return "bronze"; // 3º lugar - Bronze
  return ""; // Demais posições não têm classe especial
};
const registrarEstudo = async () => {
  if (!titulo.value.trim() || !tempo.value || tempo.value <= 0) {
    errorMessage.value = "⚠️ Preencha todos os campos corretamente!";
    successMessage.value = "";
    setTimeout(() => (errorMessage.value = ""), 3000);
    return;
  }

  isLoading.value = true;
  errorMessage.value = "";
  successMessage.value = "";

  try {
    await store.registrarEstudo(titulo.value, parseInt(tempo.value));

    // Limpa os campos e exibe mensagem de sucesso
    titulo.value = "";
    tempo.value = "";
    successMessage.value = "✅ Estudo registrado com sucesso!";
    setTimeout(() => (successMessage.value = ""), 3000);

    // Atualiza os dados após o registro
    store.fetchEstudos();
    store.fetchRanking();
  } catch (error) {
    errorMessage.value = `❌ Erro ao registrar estudo: ${
      error.response?.data?.message || error.message
    }`;
    setTimeout(() => (errorMessage.value = ""), 5000);
  }

  isLoading.value = false;
};
</script>

<template>
  <div class="page-container">
    <div class="container">
      <div class="header">
        <h1 class="welcome-title">
          👋 Bem-vindo, <span class="username">{{ nomeUsuario }}</span>
        </h1>
        <p class="subtitle">
          📊 Acompanhe seus estudos e compare seu progresso
        </p>
      </div>

      <!-- Dashboard Cards -->
      <div class="dashboard-grid">
        <!-- Seção de Registro de Estudo -->
        <div class="card register-card">
          <h2>📝 Registrar Estudo</h2>
          <div class="form-group">
            <label for="titulo">🎥 Nome do Vídeo/Material</label>
            <input
              id="titulo"
              v-model="titulo"
              placeholder="Ex: Videoaula 01 - Prof.Fulano"
              class="input"
            />
          </div>

          <div class="form-group">
            <label for="tempo">⏳ Tempo de Estudo (min)</label>
            <input
              id="tempo"
              v-model="tempo"
              type="number"
              placeholder="Ex: 45"
              class="input"
            />
          </div>

          <button @click="registrarEstudo" :disabled="isLoading" class="button">
            <span v-if="isLoading" class="loading-spinner"></span>
            {{ isLoading ? "⏳ Salvando..." : "✅ Registrar Estudo" }}
          </button>

          <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
          <p v-if="successMessage" class="success-message">
            {{ successMessage }}
          </p>
        </div>

        <!-- Ranking -->
        <div class="card ranking-card">
          <h2>🏆 Ranking de Estudos</h2>
          <table class="ranking-table">
            <thead>
              <tr>
                <th>#</th>
                <th>👤 Usuário</th>
                <th>📊 Pontos</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(user, index) in rankingOrdenado"
                :key="index"
                :class="getRankingClass(index)"
              >
                <td>{{ index + 1 }}</td>
                <td>
                  <router-link :to="'/perfil/' + user.id" class="perfil-link">
                    {{ user.usuario_nome || "Desconhecido" }}
                  </router-link>
                </td>
                <td class="points">{{ user.pontos || 0 }}</td>
              </tr>
            </tbody>
          </table>
          <p v-if="!store.ranking.length" class="empty-message">
            🚀 Ainda não há dados no ranking. Seja o primeiro!
          </p>

          <!-- 🔥 Botão para mostrar a pontuação -->
          <button class="pontuacao-toggle" @click="toggleTabelaPontuacao">
            📋 Como é calculada a pontuação?
          </button>

          <!-- 🔥 Tabela de Pontuação dentro do Ranking -->
          <div v-if="mostrarTabelaPontuacao" class="pontuacao-box">
            <table class="pontuacao-table">
              <thead>
                <tr>
                  <th>⏳ Tempo</th>
                  <th>🎯 Pontos</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1 - 30 min</td>
                  <td>10</td>
                </tr>
                <tr>
                  <td>31 - 60 min</td>
                  <td>25</td>
                </tr>
                <tr>
                  <td>61 - 120 min</td>
                  <td>50</td>
                </tr>
                <tr>
                  <td>Acima de 120 min</td>
                  <td>100</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Botão de Navegação -->
      <div class="action-buttons">
        <button @click="router.push('/meus-estudos')" class="primary-button">
          📚 Meus Estudos
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.perfil-link {
  text-decoration: none;
  color: #6a11cb;
  font-weight: bold;
}

.perfil-link:hover {
  text-decoration: underline;
}
.page-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  background-color: #f5f5f5;
  overflow-x: hidden;
}

.container {
  max-width: 900px;
  width: 100%;
  text-align: center;
  padding: 20px;
  margin-top: -220px;
}

/* 🌍 Estilização do Ranking */
.gold {
  background: gold;
  font-weight: bold;
}

.silver {
  background: silver;
  font-weight: bold;
}

.bronze {
  background: #cd7f32;
  color: white;
  font-weight: bold;
}

/* 🎨 Estilos Gerais */
.page-container {
  width: 80vw;
  height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #1a1d3a;
  padding: 0;
  margin: 0;
  overflow-x: hidden;
}

.container {
  max-width: 900px;
  width: 100%;
  text-align: center;
  margin: auto;
  margin-top: 2%;
}

/* 🏆 Header */
.header {
  margin-bottom: 20px;
}

.welcome-title {
  font-size: 45px;
  color: #ffffff;
}

.username {
  color: #6a11cb;
  font-weight: bold;
}

.subtitle {
  color: #ffffff;
  font-size: 25px;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 30px;
  align-items: flex-start; /* 🔥 Impede que os cards cresçam juntos */
}

@media (max-width: 768px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}

/* 📦 Cartões */
.card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

/* 📝 Formulário */
.register-card .form-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 15px;
}

.register-card .form-group label {
  font-weight: bold;
  margin-bottom: 5px;
  color: #333;
}

/* 📏 Inputs */
.input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  transition: all 0.3s ease;
}

/* Efeito no Input ao Focar */
.input:focus {
  border-color: #6a11cb;
  box-shadow: 0 0 8px rgba(106, 17, 203, 0.4);
}

/* 🔄 Ajuste para telas menores */
@media (max-width: 600px) {
  .input {
    font-size: 13px;
    padding: 8px;
  }
}

/* 🎯 Botões */
.button {
  width: 100%;
  max-width: 200px;
  padding: 12px;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s ease-in-out;
  text-align: center;
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

/* 📊 Ranking */
.ranking-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  font-size: 14px;
}
.ranking-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* 🔥 Mantém os elementos internos alinhados */
  min-height: 250px; /* 🔥 Define uma altura mínima */
}

.ranking-table th,
.ranking-table td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

.ranking-table th {
  background: #6a11cb;
  color: white;
}

/* 📱 Ajustando ranking para telas menores */
@media (max-width: 600px) {
  .ranking-table {
    font-size: 12px;
  }
}

/* 🎯 Botões de Ação */
.action-buttons {
  bottom: 300px; /* 🔥 Define um espaço da parte inferior */
  left: 67%; /* 🔥 Centraliza o botão */
  transform: translateX(-50%); /* 🔥 Mantém alinhado no centro */
  width: 100%;
  display: flex;
  justify-content: center;
  gap: 15px;
}

/* 🔥 Botão "Meus Estudos" */
.primary-button {
  background: #6a11cb;
  color: white;
  width: 300px;
  padding: 18px;
  font-size: 1.3rem;
  border-radius: 25px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  text-align: center;
  transform: scale(1);
  margin-left: 150%;
}

/* 🚀 Animação ao passar o mouse */
.primary-button:hover {
  background: #5907a5;
  transform: scale(1.05);
}

/* ⏬ Efeito ao clicar */
.primary-button:active {
  transform: scale(0.95);
}

/* 🔄 Ajustes para telas menores */
@media (max-width: 600px) {
  .action-buttons {
    flex-direction: column;
    width: 100%;
    gap: 10px;
  }

  .primary-button {
    width: 100%;
    font-size: 1.2rem;
    padding: 16px;
  }
}

/* 🔹 Estilo dos Inputs no Formulário */
.register-card .form-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.register-card .form-group label {
  font-weight: bold;
  margin-bottom: 5px;
  color: #333;
  text-align: left;
  width: 100%;
  max-width: 300px;
}

.register-card .input {
  width: 100%;
  max-width: 300px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
}
.pontuacao-card {
  position: absolute;
  bottom: 20px;
  right: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  padding: 10px;
  max-width: 250px;
  font-size: 14px;
  text-align: center;
}

.pontuacao-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}

.info-text {
  font-size: 14px;
  color: #555;
  margin-bottom: 15px;
}

.pontuacao-toggle {
  margin-top: 30px;
  padding: 10px;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 25px;
  font-weight: bold;
  cursor: pointer;
  width: 50%;
  transition: 0.3s;
}

.pontuacao-toggle:hover {
  background-color: #5907a5;
}

/* 🔥 Caixa da Tabela de Pontuação */
.pontuacao-box {
  margin-top: 15px;
  background: white;
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

/* 🔥 Estilização da Tabela */
.pontuacao-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}

.pontuacao-table th,
.pontuacao-table td {
  padding: 8px;
  border: 1px solid #ddd;
  text-align: center;
}

.pontuacao-table th {
  background: #6a11cb;
  color: white;
}

.pontuacao-table td {
  background: #f9f9f9;
}

/* 📱 Ajustes responsivos */
@media (max-width: 768px) {
  .pontuacao-table {
    font-size: 12px;
  }

  .pontuacao-table th,
  .pontuacao-table td {
    padding: 6px;
  }
}
</style>
