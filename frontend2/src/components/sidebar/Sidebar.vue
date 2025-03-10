<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from "vue";
import { useRouter } from "vue-router";
import api from "../../api";

const router = useRouter();
const isMobile = ref(window.innerWidth <= 768);
const collapsed = ref(isMobile.value);
const showMobileSidebar = ref(false);

// 🔥 Armazena os dados do usuário
const usuario = ref(null);
const progresso = ref(0);

// Obtém os dados do usuário autenticado
const carregarUsuario = async () => {
  try {
    const usuarioId = localStorage.getItem("usuario_id");
    if (!usuarioId) return;

    const response = await api.get(`/usuarios/${usuarioId}/perfil/`);
    usuario.value = response.data;
    progresso.value = response.data.progresso_porcentagem;
  } catch (error) {
    console.error("Erro ao carregar perfil:", error);
  }
};

onMounted(() => {
  carregarUsuario();
  window.addEventListener("resize", handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", handleResize);
});

const sidebarWidth = computed(() => (collapsed.value ? "80px" : "250px"));

const toggleSidebar = () => {
  collapsed.value = !collapsed.value;
};

const toggleMobileSidebar = () => {
  showMobileSidebar.value = !showMobileSidebar.value;
};

const logout = () => {
  localStorage.removeItem("usuario_nome");
  localStorage.removeItem("usuario_id");
  router.push("/");
};

const handleResize = () => {
  isMobile.value = window.innerWidth <= 768;
  if (isMobile.value) {
    collapsed.value = true;
    showMobileSidebar.value = false;
  }
};
</script>

<template>
  <div>
    <!-- 🔥 Botão de Menu para Mobile -->
    <button v-if="isMobile" class="menu-button" @click="toggleMobileSidebar">
      ☰
    </button>

    <!-- 🌟 Sidebar Desktop -->
    <div class="sidebar" v-if="!isMobile" :style="{ width: sidebarWidth }">
      <h1 class="sidebar-title">
        <span v-if="collapsed"> ES </span>
        <span v-else> EstudaSync </span>
      </h1>

      <!-- 🔥 Informações do Usuário -->
      <div class="user-info" v-if="usuario">
        <p class="username"><i class="fas fa-user"></i> {{ usuario.nome }}</p>

        <!-- 🔥 Barra de Progresso -->
        <div class="progress-container">
          <p class="progress-label">Progresso: {{ progresso.toFixed(2) }}%</p>
          <div class="progress-bar">
            <div
              class="progress-fill"
              :style="{ width: progresso + '%' }"
            ></div>
          </div>
        </div>

        <!-- 🔥 Botão Meu Perfil -->
        <button
          class="profile-button"
          @click="router.push(`/perfil/${usuario.id}`)"
        >
          <i class="fas fa-user-circle"></i> Meu Perfil
        </button>
      </div>

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

    <!-- 🔥 Sidebar Mobile -->
    <div class="mobile-sidebar" v-if="isMobile && showMobileSidebar">
      <button class="close-button" @click="toggleMobileSidebar">✖</button>
      <h1 class="sidebar-title">EstudaSync</h1>

      <div class="user-info" v-if="usuario">
        <p class="username"><i class="fas fa-user"></i> {{ usuario.nome }}</p>

        <div class="progress-container">
          <p class="progress-label">Progresso: {{ progresso.toFixed(2) }}%</p>
          <div class="progress-bar">
            <div
              class="progress-fill"
              :style="{ width: progresso + '%' }"
            ></div>
          </div>
        </div>

        <button
          class="profile-button"
          @click="router.push(`/perfil/${usuario.id}`)"
        >
          <i class="fas fa-user-circle"></i> Meu Perfil
        </button>
      </div>

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
.user-info {
  text-align: center;
  margin-bottom: 20px;
}

.username {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 10px;
  margin-top: 0px;
}

.progress-container {
  width: 100%;
  max-width: 200px;
  margin: 0 auto 10px;
}

.progress-label {
  font-size: 0.9rem;
  color: #f0f0f0;
}

.progress-bar {
  width: 100%;
  height: 10px;
  background-color: #444;
  border-radius: 5px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background-color: #38a169;
  transition: width 0.5s ease-in-out;
}

.profile-button {
  width: 100%;
  padding: 10px;
  background-color: #38a169;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s ease-in-out;
}

.profile-button:hover {
  background-color: #2f855a;
}
</style>
