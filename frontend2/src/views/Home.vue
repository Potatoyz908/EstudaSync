<script setup>
import { ref, onMounted, watchEffect } from "vue";
import { useEstudaSyncStore } from "../store/estudasyncStore";
import { useRouter } from "vue-router";

const store = useEstudaSyncStore();
const router = useRouter();
const nomeUsuario = ref("Usuário");

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

const titulo = ref("");
const tempo = ref("");
const isLoading = ref(false);
const errorMessage = ref("");
const successMessage = ref("");

const registrarEstudo = async () => {
  if (titulo.value && tempo.value > 0) {
    isLoading.value = true;
    errorMessage.value = "";

    try {
      await store.registrarEstudo(titulo.value, parseInt(tempo.value));
      titulo.value = "";
      tempo.value = "";
      successMessage.value = "Estudo registrado com sucesso!";
      setTimeout(() => (successMessage.value = ""), 3000);
    } catch (error) {
      errorMessage.value = "Erro ao registrar estudo!";
    }
    isLoading.value = false;
  } else {
    errorMessage.value = "Preencha todos os campos!";
    setTimeout(() => (errorMessage.value = ""), 3000);
  }
};

// 🔥 FUNÇÃO PARA DEFINIR CLASSE DO RANKING 🔥
const getRankingClass = (index) => {
  if (index === 0) return "gold"; // 1º lugar - Ouro
  if (index === 1) return "silver"; // 2º lugar - Prata
  if (index === 2) return "bronze"; // 3º lugar - Bronze
  return ""; // Demais posições não têm classe especial
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
              placeholder="Ex: Aula de Vue.js"
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
                v-for="(user, index) in store.ranking"
                :key="user.id"
                :class="getRankingClass(index)"
              >
                <td>{{ index + 1 }}</td>
                <td>{{ user.usuario }}</td>
                <td class="points">{{ user.pontos }}</td>
              </tr>
            </tbody>
          </table>
          <p v-if="!store.ranking.length" class="empty-message">
            🚀 Ainda não há dados no ranking. Seja o primeiro!
          </p>
        </div>
      </div>

      <!-- Botões de navegação -->
      <div class="action-buttons">
        <button @click="router.push('/meus-estudos')" class="primary-button">
          📚 Meus Estudos
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  background-color: #f5f5f5; /* 🔥 Define um fundo consistente */
  overflow-x: hidden; /* 🔥 Evita scroll lateral */
}

.container {
  max-width: 900px;
  width: 100%;
  text-align: center;
  padding: 20px;
  margin-top: -220px; /* 🔥 Ajuste o valor conforme necessário */
}

/* Garante que o conteúdo se ajuste corretamente */
.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 30px;
}

/* Ajustes para telas menores */
@media (max-width: 768px) {
  .dashboard-grid {
    grid-template-columns: 1fr; /* 🔥 Mantém os elementos alinhados no mobile */
  }
}
/* 🌍 Cores para o ranking */
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

/* 🎨 Estilos gerais */
.page-container {
  width: 80vw; /* 🔥 Ocupa toda a largura */
  height: 50vh; /* 🔥 Ocupa toda a altura */
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #1a1d3a; /* 🔥 Mude conforme necessário */
  padding: 0;
  margin: 0;
  overflow-x: hidden;
}

.container {
  max-width: 900px;
  width: 100%;
  text-align: center;
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

/* 📱 Ajustando a grade para responsividade */
.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 30px;
}

/* 🔄 Estilos para dispositivos menores */
@media (max-width: 768px) {
  .dashboard-grid {
    grid-template-columns: 1fr; /* Fica em uma única coluna */
  }
}

/* 📦 Cartões */
.card {
  background: rgb(255, 255, 255);
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

/* 📝 Formulário de registro de estudo */
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
}

/* 🔄 Ajuste para telas menores */
@media (max-width: 600px) {
  .input {
    font-size: 13px;
    padding: 8px;
  }
}

/* 🎯 Botão de registro */
.button {
  width: 100%;
  max-width: 200px;
  padding: 12px;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
  text-align: center;
}

.button:hover {
  background-color: #5907a5;
}

/* 🚀 Responsividade dos botões */
@media (max-width: 600px) {
  .button {
    font-size: 14px;
    padding: 10px;
  }
}

/* 📊 Ranking */
.ranking-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  font-size: 14px;
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

/* 🎯 Botões de ação */
.action-buttons {
  display: flex;
  justify-content: center;
  gap: 15px;
}

/* 🔥 Aumento do botão "Meus Estudos" */
.primary-button {
  background: #6a11cb;
  color: white;
  width: 300px; /* 🔥 Largura maior */
  padding: 18px; /* 🔥 Aumenta a altura */
  font-size: 1.3rem; /* 🔥 Texto maior */
  border-radius: 10px; /* 🔥 Bordas arredondadas */
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s;
  border: none;
  text-align: center;
}

.primary-button:hover {
  background: #5907a5;
}

/* 🔄 Ajustes para telas menores */
@media (max-width: 600px) {
  .action-buttons {
    flex-direction: column;
    width: 100%;
    gap: 10px;
  }
  .primary-button {
    width: 100%; /* 🔥 Ocupa toda a largura */
    font-size: 1.2rem; /* 🔥 Ajuste de texto */
    padding: 16px;
  }
}

.register-card .form-group {
  display: flex;
  flex-direction: column;
  align-items: center; /* Centraliza os inputs */
  margin-bottom: 15px;
}

.register-card .form-group label {
  font-weight: bold;
  margin-bottom: 5px;
  color: #333;
  text-align: left;
  width: 100%;
  max-width: 300px; /* Limita a largura do label */
}

.register-card .input {
  width: 100%;
  max-width: 300px; /* 🔥 Define um limite de largura */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
}
</style>
