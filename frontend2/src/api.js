import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // Ajuste conforme necessário
  headers: {
    "Content-Type": "application/json",
  },
});

export const loginUsuario = async (nome) => {
  try {
    const response = await api.post("/login/", { nome });
    localStorage.setItem("usuario_id", response.data.id);
    localStorage.setItem("usuario_nome", response.data.nome);
    return response.data;
  } catch (error) {
    console.error("Erro no login:", error);
    return null;
  }
};

export default api;
