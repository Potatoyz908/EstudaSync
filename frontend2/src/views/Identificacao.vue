<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const nomeUsuario = ref("");
const isLoading = ref(false);
const error = ref("");

const salvarNome = () => {
  if (nomeUsuario.value.trim()) {
    isLoading.value = true;
    setTimeout(() => {
      localStorage.setItem("usuario", nomeUsuario.value.trim());
      router.push("/home");
      isLoading.value = false;
    }, 800); // Simulando um pequeno delay para mostrar o loading
  } else {
    error.value = "Por favor, digite seu nome";
    setTimeout(() => {
      error.value = "";
    }, 3000);
  }
};
</script>

<template>
  <div
    class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-indigo-600 to-blue-500 p-4"
  >
    <div class="w-full max-w-md bg-white rounded-xl shadow-xl overflow-hidden">
      <div class="p-8">
        <div class="flex justify-center mb-6">
          <div class="bg-indigo-100 p-3 rounded-full">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-10 w-10 text-indigo-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            ></svg>
          </div>
        </div>
        <h1 class="text-3xl font-extrabold text-center text-gray-800 mb-2">
          Bem-vindo!
        </h1>
        <p class="text-center text-gray-500 mb-8">
          Entre no EstudaSync para acompanhar seu progresso.
        </p>

        <div class="space-y-4">
          <div>
            <label
              for="nome"
              class="block text-sm font-medium text-gray-700 mb-1"
              >Nome</label
            >
            <input
              id="nome"
              v-model="nomeUsuario"
              @keyup.enter="salvarNome"
              placeholder="Digite seu nome"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors duration-200"
              :class="{ 'border-red-500': error }"
            />
            <p v-if="error" class="mt-1 text-sm text-red-600">{{ error }}</p>
          </div>

          <button
            @click="salvarNome"
            class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-3 px-4 rounded-lg transition-colors duration-200 flex items-center justify-center"
            :disabled="isLoading"
          >
            <svg
              v-if="isLoading"
              class="animate-spin -ml-1 mr-2 h-4 w-4 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>
              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
            <span>{{ isLoading ? "Entrando..." : "Entrar" }}</span>
          </button>
        </div>
      </div>

      <div
        class="px-8 py-4 bg-gray-50 border-t border-gray-100 flex justify-center"
      >
        <p class="text-xs text-gray-500">
          © {{ new Date().getFullYear() }} EstudaSync. Todos os direitos
          reservados.
        </p>
      </div>
    </div>
  </div>
</template>
