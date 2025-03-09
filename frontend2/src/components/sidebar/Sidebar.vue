<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const isMobile = ref(window.innerWidth <= 768);
const collapsed = ref(isMobile.value);
const showMobileSidebar = ref(false); // Estado para abrir/fechar o menu mobile

const sidebarWidth = computed(() => (collapsed.value ? "80px" : "250px"));

const toggleSidebar = () => {
  collapsed.value = !collapsed.value;
};

// Alternar o menu lateral para mobile
const toggleMobileSidebar = () => {
  showMobileSidebar.value = !showMobileSidebar.value;
};

// Função de logout
const logout = () => {
  localStorage.removeItem("usuario_nome");
  localStorage.removeItem("usuario_id");
  router.push("/");
};

// Atualiza o estado se a tela for redimensionada
const handleResize = () => {
  isMobile.value = window.innerWidth <= 768;
  if (isMobile.value) {
    collapsed.value = true; // Fecha a sidebar desktop no mobile
    showMobileSidebar.value = false; // Fecha o menu mobile ao redimensionar
  }
};

// Adiciona e remove o listener de redimensionamento
onMounted(() => {
  window.addEventListener("resize", handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", handleResize);
});
</script>

<template>
  <div>
    <!-- 🔥 Botão de Menu para Mobile -->
    <button v-if="isMobile" class="menu-button" @click="toggleMobileSidebar">
      ☰
    </button>

    <!-- 🌟 Sidebar Desktop (Mantida) -->
    <div class="sidebar" v-if="!isMobile" :style="{ width: sidebarWidth }">
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

    <!-- 🔥 Sidebar Mobile (Nova) -->
    <div class="mobile-sidebar" v-if="isMobile && showMobileSidebar">
      <button class="close-button" @click="toggleMobileSidebar">✖</button>
      <h1 class="sidebar-title">EstudaSync</h1>

      <nav>
        <button @click="router.push('/home')" class="sidebar-link">
          <i class="fas fa-home"></i> Página Inicial
        </button>
        <button @click="router.push('/meus-estudos')" class="sidebar-link">
          <i class="fas fa-book"></i> Meus Estudos
        </button>
      </nav>

      <button @click="logout" class="logout-button">
        <i class="fas fa-sign-out-alt"></i> Sair
      </button>
    </div>

    <!-- 🔥 Sobreposição no fundo ao abrir o menu -->
    <div
      v-if="showMobileSidebar"
      class="overlay"
      @click="toggleMobileSidebar"
    ></div>
  </div>
</template>

<style scoped>
/* 🌟 Sidebar Desktop */
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
  border-radius: 25px;
}

.logout-button {
  background: none;
  border: none;
  color: white;
  width: 80%;
  padding: 15px;
  text-align: left;
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: 1.6rem;
}

.logout-button:hover {
  background-color: #e53e3e;
  border-radius: 25px;
}

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

/* 🔥 Botão de menu para dispositivos móveis */
.menu-button {
  display: none;
  position: fixed;
  top: 15px;
  left: 15px;
  font-size: 24px;
  background: none;
  border: none;
  color: #2f855a;
  cursor: pointer;
  z-index: 1100;
}

@media (max-width: 768px) {
  .menu-button {
    display: block;
  }

  .sidebar {
    display: none; /* 🔥 Esconde a sidebar desktop em mobile */
  }
}

/* 🌟 Sidebar Mobile */
.mobile-sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 250px;
  height: 100%;
  background-color: #2f855a;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  z-index: 1200;
  transform: translateX(0);
  transition: transform 0.3s ease-in-out;
}

/* ❌ Botão para fechar o menu */
.close-button {
  align-self: flex-end;
  background: none;
  border: none;
  font-size: 24px;
  color: white;
  cursor: pointer;
  margin-bottom: 10px;
}

/* 🔥 Sobreposição no fundo ao abrir o menu */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1100;
}
</style>
