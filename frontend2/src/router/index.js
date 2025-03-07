import { createRouter, createWebHistory } from "vue-router";
import Identificacao from "@/views/Identificacao.vue";
import Home from "@/views/Home.vue";
import MeusEstudos from "@/views/MeusEstudos.vue";

const routes = [
  { path: "/", component: Identificacao },
  { path: "/home", component: Home },
  { path: "/meus-estudos", component: MeusEstudos },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
