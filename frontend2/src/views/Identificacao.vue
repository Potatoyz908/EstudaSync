<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { loginUsuario } from "../api"; // Faz login no backend e salva no banco

const router = useRouter();
const nomeUsuario = ref("");
const isLoading = ref(false);
const error = ref("");

const salvarNome = async () => {
  if (nomeUsuario.value.trim()) {
    isLoading.value = true;

    const user = await loginUsuario(nomeUsuario.value.trim());

    if (user) {
      router.push("/home");
    } else {
      error.value = "Erro ao fazer login. Tente novamente!";
      isLoading.value = false;
    }
  } else {
    error.value = "Por favor, digite seu nome!";
    setTimeout(() => (error.value = ""), 3000);
  }
};
</script>

<template>
  <div class="container">
    <div class="login-box">
      <div class="logo-container">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="logo"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
          />
        </svg>
      </div>

      <h1 class="title">Bem-vindo ao EstudaSync 🎓</h1>
      <p class="subtitle">Digite seu nome para acessar a plataforma.</p>

      <input
        v-model="nomeUsuario"
        @keyup.enter="salvarNome"
        placeholder="✍️ Digite seu nome"
        class="input"
      />
      <p v-if="error" class="error">⚠️ {{ error }}</p>

      <button @click="salvarNome" :disabled="isLoading" class="button">
        <span v-if="isLoading">🔄 Entrando...</span>
        <span v-else>🚀 Entrar</span>
      </button>
    </div>

    <p class="footer">
      © {{ new Date().getFullYear() }} EstudaSync. Todos os direitos reservados.
    </p>
  </div>
</template>
<style scoped>
/* 🌟 Layout Principal */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: #1a1d3a; /* 🔥 Cor de fundo padronizada */
  text-align: center;
  margin: 0;
  padding: 0;
  overflow: hidden; /* 🔥 Evita rolagem */
}

/* 📦 Caixa de Login */
.login-box {
  position: absolute; /* 🔥 Mantém a posição fixa */
  top: 40%; /* 🔥 Move para o centro verticalmente */
  left: 50%; /* 🔥 Move para o centro horizontalmente */
  transform: translate(-50%, -50%); /* 🔥 Ajuste fino para centralizar */

  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 90%; /* 🔥 Ajuste para telas menores */
  max-width: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  transition: transform 0.3s ease-in-out;
}

/* 🎨 Ícone/Logo */
.logo-container {
  display: flex;
  justify-content: center;
  margin-bottom: 15px;
}
.logo {
  height: 50px;
  color: #6a11cb;
}

/* 🏆 Título e Subtítulo */
.title {
  font-size: 26px;
  font-weight: bold;
  color: #333;
}
.subtitle {
  font-size: 14px;
  color: #666;
  margin-bottom: 15px;
}

/* 📝 Input */
.input {
  width: 90%;
  padding: 12px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 16px;
  transition: border 0.3s ease-in-out;
}

/* 🔥 Foco no Input */
.input:focus {
  border: 2px solid #6a11cb;
  outline: none;
}

/* 🚀 Botão */
.button {
  width: 100%;
  max-width: 200px;
  padding: 14px;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 25px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  transform: scale(1);
}

/* 🖱️ Animação ao passar o mouse */
.button:hover {
  background-color: #5907a5;
  transform: scale(1.05);
}

/* ⏬ Efeito ao clicar */
.button:active {
  transform: scale(0.95);
}

/* 🚫 Botão Desativado */
.button:disabled {
  background-color: #999;
  cursor: not-allowed;
}

/* ⚠️ Mensagem de Erro */
.error {
  color: red;
  font-size: 14px;
  font-weight: bold;
}

/* 📜 Rodapé */
.footer {
  position: absolute; /* 🔥 Mantém o footer fixo na parte inferior */
  bottom: 20px; /* 🔥 Define um espaço da parte inferior */
  left: 50%; /* 🔥 Centraliza horizontalmente */
  top: 58%; /* 🔥 Centraliza verticalmente */
  transform: translateX(-50%); /* 🔥 Ajuste fino para alinhamento central */
  font-size: 12px;
  color: #dcdcdc;
  text-align: center;
  width: 100%;
}
</style>
