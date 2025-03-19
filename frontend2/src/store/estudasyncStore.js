import { defineStore } from "pinia";
import api from "../api";

export const useEstudaSyncStore = defineStore("estudasync", {
  state: () => ({
    estudos: [],
    ranking: [],
    usuarioId: localStorage.getItem("usuario_id") || null,
    mostrarTodosEstudos: false, // 🔥 Novo estado para alternar a exibição
  }),
  actions: {
    async fetchEstudos() {
      try {
        let url = "/estudos/";
        if (!this.mostrarTodosEstudos && this.usuarioId) {
          url += `?usuario_id=${this.usuarioId}`;
        }
        const res = await api.get(url);
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
    async editarEstudo(estudoId, novoTitulo, novoTempo) {
      try {
        const usuarioId = this.usuarioId; // Pega o usuário logado

        await api.put(`/estudos/${estudoId}/`, {
          usuario_id: parseInt(usuarioId), // ✅ Adiciona o usuário na requisição
          titulo: novoTitulo,
          tempo_estudado: parseInt(novoTempo),
        });
        console.log(`Estudo ${estudoId} atualizado com sucesso!`);
        this.fetchEstudos(); // Atualiza a lista após edição
      } catch (error) {
        console.error(
          "Erro ao editar estudo:",
          error.response?.data || error.message
        );
      }
    },
    async excluirEstudo(estudoId) {
      try {
        await api.delete(`/estudos/${estudoId}/`);
        console.log(`Estudo ${estudoId} excluído com sucesso!`);
        this.fetchEstudos(); // Atualiza a lista após exclusão
      } catch (error) {
        console.error(
          "Erro ao excluir estudo:",
          error.response?.data || error.message
        );
      }
    },
    alternarFiltroEstudos() {
      this.mostrarTodosEstudos = !this.mostrarTodosEstudos;
      this.fetchEstudos(); // 🔥 Atualiza a lista de estudos após a alteração
    },
  },
});
