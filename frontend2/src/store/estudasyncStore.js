import { defineStore } from "pinia";
import api from "../api";

export const useEstudaSyncStore = defineStore("estudasync", {
  state: () => ({
    estudos: [],
    ranking: [],
    usuarioId: localStorage.getItem("usuario_id") || null,
  }),
  actions: {
    async fetchEstudos() {
      if (!this.usuarioId) return;
      try {
        const res = await api.get(`/estudos/?usuario_id=${this.usuarioId}`);
        this.estudos = res.data;
      } catch (error) {
        console.error(
          "Erro ao buscar estudos:",
          error.response?.data || error.message
        );
      }
    },
    async fetchRanking() {
      try {
        const res = await api.get("/pontuacoes/");
        this.ranking = res.data;
      } catch (error) {
        console.error(
          "Erro ao buscar ranking:",
          error.response?.data || error.message
        );
      }
    },
    async registrarEstudo(titulo, tempo) {
      if (!this.usuarioId) {
        console.error("Erro: Usuário não identificado");
        return;
      }
      try {
        const response = await api.post("/estudos/", {
          usuario_id: parseInt(this.usuarioId), // 🔥 Agora enviamos `usuario_id` corretamente
          titulo: titulo,
          tempo_estudado: tempo,
        });
        console.log("Estudo registrado:", response.data);
        this.fetchEstudos();
        this.fetchRanking();
      } catch (error) {
        console.error(
          "Erro ao registrar estudo:",
          error.response?.data || error.message
        );
      }
    },
  },
});
