<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const isMobile = ref(window.innerWidth <= 768); // Detecta se é mobile
const collapsed = ref(isMobile.value); // Se for mobile, inicia fechada
const sidebarWidth = computed(() => (collapsed.value ? "80px" : "250px"));

const toggleSidebar = () => {
  collapsed.value = !collapsed.value;
};

// Função de logout
const logout = () => {
  localStorage.removeItem("usuario_nome");
  localStorage.removeItem("usuario_id");
  router.push("/"); // Redireciona para a página inicial
};

// Atualiza o estado se a tela for redimensionada
window.addEventListener("resize", () => {
  isMobile.value = window.innerWidth <= 768;
  if (isMobile.value) collapsed.value = true; // Fecha a sidebar no mobile
});
</script>

<template>
  <div>
    <!-- Ícone de Menu para Mobile -->
    <button v-if="isMobile" class="menu-button" @click="toggleSidebar">
      ☰
    </button>

    <div class="sidebar" :style="{ width: sidebarWidth }">
      <h1 class="sidebar-title">
        <span v-if="collapsed"> ES </span>
        <span v-else> EstudaSync </span>
      </h1>

      <nav>
        <button @click="router.push('/home')" class="sidebar-link">
          <i class="fas fa-home"></i>
          <span v-if="!collapsed"> Página Inicial </span>
        </button>
        <button @click="router.push('/meus-estudos')" class="sidebar-link">
          <i class="fas fa-book"></i>
          <span v-if="!collapsed"> Meus Estudos </span>
        </button>
      </nav>

      <!-- 🔥 Botão de Logout -->
      <button @click="logout" class="logout-button">
        <i class="fas fa-sign-out-alt"></i>
        <span v-if="!collapsed"> Sair </span>
      </button>

      <span
        class="collapse-icon"
        :class="{ 'rotate-180': collapsed }"
        @click="toggleSidebar"
      >
        <i class="fas fa-angle-double-left"></i>
      </span>
    </div>
  </div>
</template>

<style scoped>
/* Sidebar */
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 1rem;
  width: 250px;
  background-color: #2f855a;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: width 0.3s ease;
  z-index: 1000;
  overflow-x: hidden;
}

.sidebar-title {
  font-weight: bold;
  text-align: center;
  font-size: 2.6rem;
}

.sidebar-link {
  background: none;
  border: none;
  color: white;
  width: 100%;
  padding: 15px;
  text-align: left;
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: 1.6rem;
}

.sidebar-link i {
  margin-right: 10px;
}

.sidebar-link:hover {
  background-color: #38a169;
}

/* 🔥 Estilização do botão de Logout */
.logout-button {
  background: none;
  border: none;
  color: white;
  width: 100%;
  padding: 15px;
  text-align: left;
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: 1.6rem;
}

.logout-button i {
  margin-right: 10px;
}

.logout-button:hover {
  background-color: #e53e3e;
}

/* Ícone de colapso da sidebar */
.collapse-icon {
  position: absolute;
  bottom: 20px;
  cursor: pointer;
  color: rgba(255, 255, 255, 0.7);
  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
}

/* Botão de menu para dispositivos móveis */
.menu-button {
  display: none;
  position: absolute;
  top: 15px;
  left: 15px;
  font-size: 24px;
  background: none;
  border: none;
  color: #2f855a;
  cursor: pointer;
  z-index: 1100;
}

/* Esconde a sidebar em telas menores */
@media (max-width: 768px) {
  .sidebar {
    width: 80px;
    transition: width 0.3s ease;
  }

  .menu-button {
    display: block;
  }
}
</style>
