<script setup>
import Navbar from "./components/Navbar.vue";
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <!-- Navbar fixa no topo -->
    <Navbar />

    <!-- Conteúdo principal ocupando todo o espaço abaixo da navbar -->
    <main class="flex-grow container mx-auto p-6 mt-16">
      <router-view />
    </main>
  </div>
</template>

<style>
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
}
</style>
