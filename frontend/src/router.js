import { createRouter, createWebHistory } from "vue-router";
import Identificacao from "./pages/Identificacao.vue";
import Home from "./pages/Home.vue";
import MeusEstudos from "./pages/MeusEstudos.vue";

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
