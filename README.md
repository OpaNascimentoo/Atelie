# Ateliê Bella — Sistema Web para Gerenciamento de Ateliê de Costura

Aplicação web desenvolvida para auxiliar no gerenciamento das atividades de um ateliê de costura, centralizando informações de **clientes, produtos, doações e encomendas** em um único ambiente.

O projeto conta com uma interface web responsiva integrada a um **backend desenvolvido em Python e Flask**, permitindo operações de cadastro, consulta, atualização e exclusão (CRUD).

🌐 **Acesse o projeto:** https://atelie-nlso.onrender.com/

---

## 🎯 Objetivo

O Ateliê Bella foi desenvolvido com o objetivo de oferecer uma solução digital para organizar as principais informações e atividades de um ateliê de costura.

A aplicação mantém uma interface visual inspirada no conceito de alta costura e integra essa interface a um backend responsável pelo processamento e gerenciamento dos dados.

Atualmente, os dados são armazenados de forma temporária em arquivos **JSON**, permitindo o funcionamento completo das operações do sistema. A integração com um banco de dados está prevista como uma evolução futura do projeto.

---

## 🚀 Funcionalidades

### 👤 Clientes

- Cadastro de clientes
- Consulta de clientes
- Edição de informações
- Exclusão de registros

### 🧵 Vitrine

- Cadastro de produtos
- Consulta de produtos
- Edição de produtos
- Exclusão de produtos
- Organização dos produtos apresentados pelo ateliê

### 🎁 Doações

- Cadastro de doações
- Consulta de registros
- Edição de informações
- Exclusão de registros

### 📦 Encomendas

- Cadastro de encomendas
- Consulta de encomendas
- Edição de informações
- Exclusão de registros
- Gerenciamento do status das encomendas

### 📊 Dashboard

- Visualização geral das informações
- Organização das encomendas por status
- Busca e consulta de registros
- Exibição de informações de clientes, serviços, peças, datas e horários
- Visualização de detalhes dos registros

---

## 🛠️ Tecnologias utilizadas

### Front-end
- HTML5
- CSS3
- JavaScript

### Back-end
- Python 3
- Flask

### Armazenamento
- JSON

### Testes
- Testes automatizados para validação das principais funcionalidades da API

---

## 🔗 Integração Front-end + Back-end

O sistema foi desenvolvido com a integração entre a interface web e uma API REST criada em Python utilizando Flask.

O front-end realiza requisições à API para consultar e modificar os dados, enquanto o backend é responsável pelo processamento das operações e pela persistência temporária das informações.

A arquitetura foi organizada de forma modular, permitindo que a aplicação possa evoluir posteriormente para a utilização de um banco de dados sem a necessidade de reconstrução completa do sistema.

---

## 📁 Estrutura do projeto

```text
Atelie/
├── backend/
│   ├── app.py
│   ├── __init__.py
│   ├── storage.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── mock_data.py
│   │   └── store.json
│   ├── models/
│   │   ├── __init__.py
│   │   └── entities.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── doacoes.py
│   │   ├── encomendas.py
│   │   ├── pedidos.py
│   │   └── vitrine.py
│   └── services/
│       ├── __init__.py
│       └── atelier_service.py
├── assets/
│   ├── produtos/
│   └── doacoes/
├── imagens/
│   ├── dashboards/
│   └── Vitrine/
├── tests/
│   └── test_backend.py
├── index.html
├── requirements.txt
└── README.md
```

---

## 💻 Como executar localmente

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd Atelie
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o backend

```bash
python backend/app.py
```

A aplicação ficará disponível localmente em:

```text
http://127.0.0.1:5000/
```

Para verificar o funcionamento da API:

```text
http://127.0.0.1:5000/api/health
```

---

## 🔌 Principais endpoints

### Pedidos

```text
GET    /api/pedidos
GET    /api/pedidos/<id>
POST   /api/pedidos
PUT    /api/pedidos/<id>
DELETE /api/pedidos/<id>
PATCH  /api/pedidos/<id>/status
```

### Clientes

```text
GET    /api/clientes
GET    /api/clientes/<id>
POST   /api/clientes
PUT    /api/clientes/<id>
DELETE /api/clientes/<id>
```

### Vitrine

```text
GET    /api/produtos
GET    /api/produtos/<id>
POST   /api/produtos
PUT    /api/produtos/<id>
DELETE /api/produtos/<id>
```

### Encomendas

```text
GET    /api/encomendas
GET    /api/encomendas/<id>
POST   /api/encomendas
PUT    /api/encomendas/<id>
DELETE /api/encomendas/<id>
```

### Doações

```text
GET    /api/doacoes
GET    /api/doacoes/<id>
POST   /api/doacoes
PUT    /api/doacoes/<id>
DELETE /api/doacoes/<id>
```

---

## 🧪 Testes

O projeto possui testes automatizados para verificar o funcionamento das principais operações do backend e da API.

Os testes podem ser executados conforme a configuração definida no projeto.

---

## 🎨 Design

A interface do Ateliê Bella foi desenvolvida com uma identidade visual inspirada no universo da alta costura.

### Características

- Design responsivo
- Interface organizada e intuitiva
- Tipografia **Cormorant Garamond** para títulos
- Tipografia **Jost** para textos
- Paleta baseada em tons de vinho, dourado, creme e carvão
- Dashboard para visualização das principais informações
- Navegação entre os diferentes módulos do sistema

---

## 💾 Persistência dos dados

Atualmente, o sistema utiliza arquivos **JSON** para armazenamento temporário dos dados.

Essa abordagem foi utilizada para permitir a implementação e demonstração das operações CRUD durante o desenvolvimento do projeto.

A utilização de um **banco de dados real** está prevista como uma etapa futura, permitindo ampliar a capacidade de armazenamento, segurança e gerenciamento das informações.

---

## 📌 Status do projeto

**Concluído nesta etapa:** ✅

- Interface web desenvolvida
- Backend em Python/Flask
- Integração entre front-end e backend
- CRUD de clientes
- CRUD de produtos
- CRUD de doações
- CRUD de encomendas
- Persistência temporária em JSON
- Testes das principais funcionalidades
- Aplicação publicada na web

### Próximos passos

- Integração com banco de dados
- Aprimoramento da persistência dos dados
- Evolução das funcionalidades de gerenciamento
- Melhorias de segurança e autenticação

---

## 🌐 Projeto online

A aplicação pode ser acessada pelo endereço:

**https://atelie-nlso.onrender.com/**

---

## 👩‍💻 Projeto acadêmico

Projeto desenvolvido como parte do **Projeto Interdisciplinar — 4º CONTEEX**, no curso de **Inteligência Artificial e Machine Learning**.

**Ateliê Bella — Sistema Web para Gerenciamento de Ateliê de Costura**
