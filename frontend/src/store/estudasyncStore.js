import { defineStore } from "pinia";
import axios from "axios";

export const useEstudaSyncStore = defineStore("estudasync", {
  state: () => ({
    estudos: [],
    ranking: [],
  }),
  actions: {
    async fetchEstudos() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/estudos/");
        this.estudos = res.data;
      } catch (error) {
        console.error("Erro ao buscar estudos:", error);
      }
    },
    async fetchRanking() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/pontuacoes/");
        this.ranking = res.data;
      } catch (error) {
        console.error("Erro ao buscar ranking:", error);
      }
    },
    async registrarEstudo(titulo, tempo) {
      try {
        await axios.post("http://127.0.0.1:8000/estudos/", {
          usuario: 1, // Substituir pelo ID do usuário autenticado depois
          titulo: titulo,
          tempo_estudado: tempo,
        });
        await this.fetchEstudos();
        await this.fetchRanking();
      } catch (error) {
        console.error("Erro ao registrar estudo:", error);
      }
    },
  },
});
