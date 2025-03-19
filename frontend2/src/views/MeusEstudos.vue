<script setup>
import { onMounted, computed, ref } from "vue";
import { useEstudaSyncStore } from "../store/estudasyncStore";
import { useRouter } from "vue-router";

const store = useEstudaSyncStore();
const router = useRouter();
const estudoEditando = ref(null); // Estado para armazenar o estudo sendo editado
const novoTitulo = ref(""); // Novo título ao editar
const novoTempo = ref(""); // Novo tempo ao editar

onMounted(() => {
  store.fetchEstudos();
});

// 🔥 Converte minutos para HH:MM:SS
const formatarTempo = (minutos) => {
  const horas = Math.floor(minutos / 60);
  const minutosRestantes = minutos % 60;
  return `${String(horas).padStart(2, "0")}:${String(minutosRestantes).padStart(
    2,
    "0"
  )}:00`;
};

// 🔥 Computed para exibir tempo total formatado
const totalTempoEstudado = computed(() => {
  const totalMinutos = store.estudos.reduce(
    (total, estudo) => total + estudo.tempo_estudado,
    0
  );
  return formatarTempo(totalMinutos);
});

// 🔥 Excluir estudo
const excluirEstudo = async (id) => {
  if (confirm("Tem certeza que deseja excluir este estudo?")) {
    await store.excluirEstudo(id);
    store.fetchEstudos();
  }
};

// 🔥 Iniciar edição
const editarEstudo = (estudo) => {
  estudoEditando.value = estudo;
  novoTitulo.value = estudo.titulo;
  novoTempo.value = estudo.tempo_estudado;
};

// 🔥 Salvar edição
const salvarEdicao = async () => {
  if (!novoTitulo.value.trim() || !novoTempo.value) {
    alert("Preencha todos os campos corretamente!");
    return;
  }

  await store.editarEstudo(
    estudoEditando.value.id,
    novoTitulo.value,
    novoTempo.value
  );
  estudoEditando.value = null;
  store.fetchEstudos();
};

// 🔥 Cancelar edição
const cancelarEdicao = () => {
  estudoEditando.value = null;
};
</script>

<template>
  <div class="container">
    <h1>📖 Meus Estudos</h1>
    <p class="total">⏳ Total: {{ totalTempoEstudado }} horas</p>

    <!-- Botão para alternar entre ver apenas os próprios estudos ou todos -->
    <button @click="store.alternarFiltroEstudos" class="toggle-button">
      {{
        store.mostrarTodosEstudos
          ? "👤 Mostrar Apenas Meus Estudos"
          : "🌍 Mostrar Todos os Estudos"
      }}
    </button>

    <ul v-if="store.estudos.length" class="estudo-list">
      <li v-for="estudo in store.estudos" :key="estudo.id" class="estudo-item">
        <div class="estudo-info">
          <span class="titulo">📚 {{ estudo.titulo }}</span> - ⏱️
          {{ formatarTempo(estudo.tempo_estudado) }}

          <!-- 🔥 Exibe o nome do usuário se não for o próprio -->
          <p
            v-if="
              store.usuarioId && estudo.usuario_id !== parseInt(store.usuarioId)
            "
            class="user-name"
          >
            👤 {{ estudo.usuario_nome || "Usuário Desconhecido" }}
          </p>
        </div>

        <!-- 🔥 Botões de edição/exclusão (Apenas para estudos do usuário) -->
        <div
          class="actions"
          v-if="
            store.usuarioId && estudo.usuario_id === parseInt(store.usuarioId)
          "
        >
          <button class="edit-button" @click="editarEstudo(estudo)">
            ✏️ Editar
          </button>
          <button class="delete-button" @click="excluirEstudo(estudo.id)">
            🗑️ Excluir
          </button>
        </div>
      </li>
    </ul>
    <p v-else class="message">⚠️ Nenhum estudo registrado ainda.</p>

    <button @click="router.push('/home')" class="button">🏠 Voltar</button>

    <!-- 🔥 Modal de Edição -->
    <div v-if="estudoEditando" class="modal">
      <div class="modal-content">
        <h2>✏️ Editar Estudo</h2>
        <label>📚 Novo Título</label>
        <input
          v-model="novoTitulo"
          class="input"
          placeholder="Digite o novo título"
        />

        <label>⏳ Novo Tempo (minutos)</label>
        <input
          v-model="novoTempo"
          type="number"
          class="input"
          placeholder="Digite o tempo"
        />

        <div class="modal-actions">
          <button @click="salvarEdicao" class="save-button">💾 Salvar</button>
          <button @click="cancelarEdicao" class="cancel-button">
            ❌ Cancelar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* 🌟 Estilização da Caixa Principal */
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
  padding: 20px;
  background: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* 🎯 Estilização do Total */
.total {
  background: #6a11cb;
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  font-weight: bold;
}

/* 🔄 Botão de Alternância */
.toggle-button {
  background-color: #6a11cb;
  color: white;
  padding: 12px 22px;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  margin: 15px 0;
  font-weight: bold;
  transition: all 0.3s ease-in-out;
  transform: scale(1);
}

/* 🚀 Animação ao passar o mouse */
.toggle-button:hover {
  background-color: #5907a5;
  transform: scale(1.05);
}

/* ⏬ Efeito ao clicar */
.toggle-button:active {
  transform: scale(0.95);
}

/* 📚 Lista de Estudos */
.estudo-list {
  list-style: none;
  padding: 0;
}

.estudo-item {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 🏷️ Estilo do Título */
.titulo {
  font-weight: bold;
}

/* 🔘 Botão de Voltar */
.button {
  width: 50%;
  padding: 14px;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 25px;
  font-size: 16px;
  margin-top: 20px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s ease-in-out;
  transform: scale(1);
}

/* 🚀 Animação ao passar o mouse */
.button:hover {
  background-color: #5907a5;
  transform: scale(1.05);
}

/* ⏬ Efeito ao clicar */
.button:active {
  transform: scale(0.95);
}
.user-name {
  font-size: 0.9rem;
  color: #555;
  margin-top: 3px;
}

/* 🔥 Botões de Ações */
.actions {
  display: flex;
  gap: 10px;
}

.edit-button,
.delete-button {
  padding: 6px 10px;
  font-size: 14px;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.edit-button {
  background: #4caf50;
  color: white;
  border: none;
}

.edit-button:hover {
  background: #388e3c;
}

.delete-button {
  background: #e53e3e;
  color: white;
  border: none;
}

.delete-button:hover {
  background: #c53030;
}

/* 🔥 Modal de Edição */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 300px;
  text-align: center;
}

.modal-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.save-button {
  background: #6a11cb;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.save-button:hover {
  background: #5907a5;
}

.cancel-button {
  background: #e53e3e;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.cancel-button:hover {
  background: #c53030;
}
</style>
