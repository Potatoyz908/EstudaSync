import { createRouter, createWebHistory } from "vue-router";
import Identificacao from "@/views/Identificacao.vue";
import Home from "@/views/Home.vue";
import MeusEstudos from "@/views/MeusEstudos.vue";
import Perfil from "@/views/Perfil.vue";

const routes = [
  { path: "/", component: Identificacao },
  { path: "/home", component: Home },
  { path: "/meus-estudos", component: MeusEstudos },
  { path: "/perfil/:id", component: Perfil, name: "perfil" }, // Rota dinâmica para o perfil do usuário,
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
