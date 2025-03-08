<script setup>
import Sidebar from "@/components/sidebar/Sidebar.vue";
import { RouterView } from "vue-router";
</script>

<template>
  <div class="layout">
    <Sidebar />
    <div class="content">
      <RouterView />
    </div>
  </div>
</template>

<style>
/* Remove margens e preenchimentos do body e html */
html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden; /* Evita rolagem indesejada */
}
</style>
