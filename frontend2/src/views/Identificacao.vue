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

      <h1 class="title">Bem-vindo ao EstudaSync</h1>
      <p class="subtitle">Digite seu nome para acessar a plataforma.</p>

      <input
        v-model="nomeUsuario"
        @keyup.enter="salvarNome"
        placeholder="Digite seu nome"
        class="input"
      />
      <p v-if="error" class="error">{{ error }}</p>

      <button @click="salvarNome" :disabled="isLoading" class="button">
        <span v-if="isLoading">Entrando...</span>
        <span v-else>Entrar</span>
      </button>
    </div>

    <p class="footer">
      © {{ new Date().getFullYear() }} EstudaSync. Todos os direitos reservados.
    </p>
  </div>
</template>

<style scoped>
/* Layout principal */
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw; /* 🔥 Garante que ocupa 100% da largura */
  background: linear-gradient(to right, #4a90e2, #6a11cb);
  text-align: center;
  margin: 0;
  padding: 0;
  overflow: hidden; /* 🔥 Garante que não haja rolagem */
}

/* Caixa de login */
.login-box {
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

/* Ícone/Logo */
.logo-container {
  display: flex;
  justify-content: center;
  margin-bottom: 15px;
}
.logo {
  height: 50px;
  color: #6a11cb;
}

/* Título e subtítulo */
.title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
}
.subtitle {
  font-size: 14px;
  color: #666;
  margin-bottom: 15px;
}

/* Input */
.input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

/* Botão */
.button {
  width: 100%;
  padding: 10px;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s ease;
}
.button:disabled {
  background-color: #999;
}

/* Mensagem de erro */
.error {
  color: red;
  font-size: 14px;
}

/* Rodapé */
.footer {
  margin-top: 20px;
  font-size: 12px;
  color: white;
}
</style>
