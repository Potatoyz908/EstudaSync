import { defineStore } from "pinia";
import api from "../api"; // Agora usamos a configuração central do Axios

export const useEstudaSyncStore = defineStore("estudasync", {
  state: () => ({
    estudos: [],
    ranking: [],
  }),
  actions: {
    async fetchEstudos() {
      try {
        const res = await api.get("/estudos/");
        this.estudos = res.data;
      } catch (error) {
        console.error("Erro ao buscar estudos:", error);
      }
    },
    async fetchRanking() {
      try {
        const res = await api.get("/pontuacoes/");
        this.ranking = res.data;
      } catch (error) {
        console.error("Erro ao buscar ranking:", error);
      }
    },
    async registrarEstudo(titulo, tempo) {
      try {
        await api.post("/estudos/", {
          usuario: localStorage.getItem("usuario"),
          titulo: titulo,
          tempo_estudado: tempo,
        });
        this.fetchEstudos();
        this.fetchRanking();
      } catch (error) {
        console.error("Erro ao registrar estudo:", error);
      }
    },
  },
});
