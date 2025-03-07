<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const collapsed = ref(false); // Controla se a sidebar está aberta ou fechada
const sidebarWidth = ref("250px");

const toggleSidebar = () => {
  collapsed.value = !collapsed.value;
  sidebarWidth.value = collapsed.value ? "80px" : "250px";
};
</script>

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1 class="text-white text-center font-bold">
      <span v-if="collapsed">
        <div>ES</div>
        <!-- EstudaSync Abreviado -->
      </span>
      <span v-else>EstudaSync</span>
    </h1>

    <nav class="mt-4">
      <button @click="router.push('/home')" class="sidebar-link">
        <i class="fas fa-home"></i>
        <span v-if="!collapsed"> Página Inicial </span>
      </button>
      <button @click="router.push('/meus-estudos')" class="sidebar-link">
        <i class="fas fa-book"></i>
        <span v-if="!collapsed"> Meus Estudos </span>
      </button>
    </nav>

    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left"></i>
    </span>
  </div>
</template>

<style>
:root {
  --sidebar-bg-color: #2f855a;
  --sidebar-item-hover: #38a169;
  --sidebar-item-active: #276749;
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);
  position: fixed;
  z-index: 100;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 1rem;
  width: 250px;
  transition: width 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sidebar h1 {
  margin-bottom: 1rem;
}

.sidebar-link {
  background: none;
  border: none;
  color: white;
  width: 100%;
  padding: 10px;
  text-align: left;
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: 1rem;
}

.sidebar-link i {
  margin-right: 10px;
}

.sidebar-link:hover {
  background-color: var(--sidebar-item-hover);
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
  transition: 0.2s linear;
}
</style>
