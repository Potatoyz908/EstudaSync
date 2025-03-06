# 📚 EstudaSync

🚀 **EstudaSync** é uma plataforma simples e motivacional para **gerenciar estudos**, permitindo que usuários registrem vídeos e materiais estudados, acompanhem seu progresso e visualizem um ranking de pontuação.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django + Django REST Framework + PostgreSQL
- **Frontend:** Vue.js + TailwindCSS + Pinia
- **Autenticação:** Armazenamento local do nome do usuário
- **Deploy:** Planejado para ser feito em plataformas como Render (backend) e Vercel (frontend)

---

## 📌 Funcionalidades

✅ **Tela de Identificação** → O usuário informa seu nome rapidamente e acessa a plataforma.  
✅ **Tela Principal** → Mostra o **ranking**, permite **registrar estudos** e tem um botão para ver "Meus Estudos".  
✅ **Tela "Meus Estudos"** → Lista todo o **histórico de estudos do usuário**.  
✅ **Pontuação baseada no esforço** → Calculada com base no **tempo estudado** e na **quantidade de materiais registrados**.  

---

## 🏗️ Como Instalar e Rodar o Projeto

### 🔹 **1. Clone o repositório**
```sh
git clone https://github.com/seu-usuario/estudasync.git
cd estudasync
```

### 🔹 **2. Configurar o Backend (Django)**

1️⃣ Entre na pasta do backend:
```sh
cd backend
```

2️⃣ Crie e ative um ambiente virtual:
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

3️⃣ Instale as dependências:
```sh
pip install -r requirements.txt
```

4️⃣ Configure o banco de dados PostgreSQL no **`backend/settings.py`**.

5️⃣ Rode as migrações e crie um superusuário (opcional):
```sh
python manage.py migrate
python manage.py createsuperuser
```

6️⃣ Inicie o backend:
```sh
python manage.py runserver
```

---

### 🔹 **3. Configurar o Frontend (Vue.js)**
1️⃣ Volte para a pasta raiz do projeto e entre no frontend:
```sh
cd ../frontend
```

2️⃣ Instale as dependências:
```sh
npm install
```

3️⃣ Inicie o servidor Vue.js:
```sh
npm run dev
```

4️⃣ Acesse no navegador:
```
http://localhost:5173
```

---

## 🚀 Como Usar

1. **Na primeira vez**, o usuário insere seu nome e entra na plataforma.
2. **Na Tela Principal**, ele pode **registrar um novo estudo** e ver o **ranking**.
3. **Na seção "Meus Estudos"**, ele pode ver seu **histórico de materiais/vídeos estudados**.

---

## 🛠️ Como Contribuir

1. Faça um **fork** do repositório.
2. Crie um **branch** para sua feature (`git checkout -b minha-feature`).
3. **Commit suas mudanças** (`git commit -m 'Minha nova feature'`).
4. **Envie para o repositório remoto** (`git push origin minha-feature`).
5. Abra um **Pull Request**.

---

💡 **Dúvidas ou sugestões?** Abra uma issue ou contribua com o projeto! 🚀🔥
```

Se precisar de alguma modificação ou quiser personalizar algo, me avise! 🚀🔥
