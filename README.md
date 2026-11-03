# Ateliê Bella — Gestão de Pedidos e Backend em Python

Aplicação web para gerenciamento do ateliê com painel visual original, estrutura de backend Flask e dados mockados para demonstrar funcionamento real do sistema.

## Objetivo

Este projeto preserva a interface visual original do ateliê, mantém a navegação e o layout do dashboard e adiciona a estrutura de backend em Python para operar clientes, produtos, encomendas, doações e pedidos.

A aplicação usa dados temporários em arquivo JSON para permitir CRUD funcional, com base pronta para evolução futura para banco de dados real.

## Tecnologias

- HTML/CSS/JavaScript
- Python 3
- Flask
- JSON para persistência temporária

## Funcionalidades

- Tela de login com validação e exibição/ocultação da senha
- Dashboard com agrupamento por status
- Cards com cliente, serviço, peça, data, horário e status
- Busca por cliente, serviço ou peça
- Estatísticas por status
- Modal de detalhes
- Navegação entre áreas do sistema
- Backend em Flask com CRUD por domínio
- Persistência em JSON em memória do projeto

## Design

- Fonte de títulos: Cormorant Garamond
- Fonte de texto: Jost
- Cores principais: vinho, dourado, creme e carvão
- Interface responsiva

## Estrutura do projeto

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
├── README.md
└── tmp_check.js
```

## Como instalar

1. Crie um ambiente virtual:

```bash
python -m venv .venv
```

2. Ative o ambiente virtual:

- Windows:

```bash
.venv\Scripts\activate
```

- Linux/macOS:

```bash
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como executar

### Backend

No Windows com Python instalado localmente:

```bash
"C:\Users\Useu\AppData\Local\Programs\Python\Python312\python.exe" backend\app.py
```

Ou, se o Python estiver no PATH:

```bash
python backend/app.py
```

A aplicação ficará disponível em:

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/api/health

## Principais endpoints

### Pedidos

- GET /api/pedidos
- GET /api/pedidos/<id>
- POST /api/pedidos
- PUT /api/pedidos/<id>
- DELETE /api/pedidos/<id>
- PATCH /api/pedidos/<id>/status

### Clientes

- GET /api/clientes
- GET /api/clientes/<id>
- POST /api/clientes
- PUT /api/clientes/<id>
- DELETE /api/clientes/<id>

### Vitrine

- GET /api/produtos
- GET /api/produtos/<id>
- POST /api/produtos
- PUT /api/produtos/<id>
- DELETE /api/produtos/<id>

### Encomendas

- GET /api/encomendas
- GET /api/encomendas/<id>
- POST /api/encomendas
- PUT /api/encomendas/<id>
- DELETE /api/encomendas/<id>

### Doações

- GET /api/doacoes
- GET /api/doacoes/<id>
- POST /api/doacoes
- PUT /api/doacoes/<id>
- DELETE /api/doacoes/<id>

## Exemplos de requisição

### Criar pedido

```bash
curl -X POST http://127.0.0.1:5000/api/pedidos \
  -H "Content-Type: application/json" \
  -d '{
    "cliente": "Maria Oliveira",
    "servico": "Ajuste de Vestido",
    "peca": "Vestido de festa",
    "data": "25 Mai 2025",
    "horario": "15:00",
    "status": "Agendado"
  }'
```

### Consultar clientes

```bash
curl http://127.0.0.1:5000/api/clientes
```

## Observações

- O sistema usa persistência temporária em JSON para demonstrar a lógica funcional do backend.
- O dashboard visual foi preservado e a API foi integrada sem substituir a base original.
- A estrutura está pronta para migrar para banco de dados real em uma etapa posterior.
- Os testes automatizados validam o comportamento crítico da API.

## Status dos pedidos

| Status | Cor |
|---|---|
| Em Produção | Laranja |
| Agendado | Índigo |
| Pronto para Prova | Roxo |
| Entregue | Verde |

## Serviços com ícone mapeado

| Serviço | Ícone |
|---|---|
| Ajuste de Vestido | Tesoura |
| Barra de Calça | Régua |
| Customização | Estrela |
| Conserto | Chave inglesa |
| Modelagem | Carretel |
| Costura | Agulha |

## Visual do projeto

O projeto foi desenvolvido para manter uma estética refinada e inspirada em alta costura, com foco em clareza, organização visual e fidelidade ao design original.

