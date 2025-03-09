<script setup>
import Sidebar from "@/components/sidebar/Sidebar.vue";
import { ref, computed, watchEffect } from "vue";

const isMobile = ref(window.innerWidth <= 768);
const sidebarOpen = ref(!isMobile.value);
const contentMargin = computed(() => (isMobile.value ? "0" : "250px"));

// Atualiza o estado ao redimensionar
watchEffect(() => {
  isMobile.value = window.innerWidth <= 768;
  if (isMobile.value) sidebarOpen.value = false;
});
</script>

<template>
  <div class="layout">
    <Sidebar />
    <div class="content" :style="{ marginLeft: contentMargin }">
      <router-view />
    </div>
  </div>
</template>

<style>
/* 🔥 Garante que toda a tela tenha o mesmo fundo */
html,
body {
  margin: 0;
  padding: 0;
  width: 100vw;
  height: 100vh;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: #1a1d3a;
}

/* 🔥 Ajusta o layout */
.layout {
  display: flex;
  width: 100vw;
  height: 100vh;
}

/* 🔥 Ajusta o conteúdo */
.content {
  flex-grow: 1;
  padding: 20px;
  transition: margin-left 0.3s ease;
  width: calc(
    100vw - 250px
  ); /* 🔥 Garante que o conteúdo ocupe o espaço certo */
  min-height: 100vh;
  background-color: transparent;
}

/* 🔥 No mobile, evita que o conteúdo fique escondido */
@media (max-width: 768px) {
  .content {
    width: 100%;
    margin-left: 0 !important;
    padding: 15px;
  }
}
</style>
