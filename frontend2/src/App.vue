<script setup>
import Sidebar from "@/components/sidebar/Sidebar.vue";
import { ref, computed } from "vue";

const isMobile = ref(window.innerWidth <= 768);
const collapsed = ref(isMobile.value);
const contentMargin = computed(() => (collapsed.value ? "80px" : "250px"));

// Atualiza o estado se a tela for redimensionada
window.addEventListener("resize", () => {
  isMobile.value = window.innerWidth <= 768;
  if (isMobile.value) collapsed.value = true;
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
  overflow: hidden;
  overflow-x: hidden; /* 🔥 Evita rolagem lateral */
  background-color: #1a1d3a; /* 🔥 ALTERE PARA A COR QUE DESEJAR */
}

/* 🔥 Ajusta o layout para preencher a tela */
.layout {
  display: flex;
  width: 100vw;
  height: 100vh;
}

/* 🔥 Ajusta o conteúdo para não herdar fundo branco */
.content {
  flex-grow: 1;
  padding: 20px;
  transition: margin-left 0.3s ease;
  width: 100%;
  min-height: 100vh;
  background-color: transparent; /* 🔥 EVITA FUNDO BRANCO */
}

/* 🔥 No mobile, garante que não fique espaço lateral */
@media (max-width: 768px) {
  .content {
    margin-left: 0 !important;
    padding: 10px;
  }
}
</style>
