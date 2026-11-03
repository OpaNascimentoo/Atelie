# Ateliê Bella — Backend em Python

## Objetivo

Este projeto evolui o sistema de gerenciamento de um ateliê de costura para a etapa de backend em Python, mantendo o front-end visual já desenvolvido e preparando a aplicação para integração futura com banco de dados.

> A aplicação já está funcionando com dados em arquivo JSON temporário, mantendo a estrutura pronta para migração para banco de dados real em uma etapa posterior.

## Tecnologias utilizadas

- HTML/CSS/JavaScript
- Python 3
- Flask

## Estrutura de pastas

```text
Atelie/
├── backend/
│   ├── app.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── mock_data.py
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
├── index.html.html
├── requirements.txt
├── README.md
└── tests/
    └── test_backend.py
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

## Como executar o backend

No ambiente Windows com Python instalado localmente:

```bash
"C:\Users\Useu\AppData\Local\Programs\Python\Python312\python.exe" backend\app.py
```

Ou, se o Python estiver no PATH:

```bash
python backend/app.py
```

A API ficará disponível em:

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/api/health

## Como executar o front-end

O projeto mantém o front-end em HTML estático. Após iniciar o backend, abra a aplicação em:

```text
http://127.0.0.1:5000/
```

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

## Exemplos de resposta

```json
{
  "id": 1,
  "cliente": "Ana Carolina Silva",
  "servico": "Ajuste de Vestido",
  "peca": "Vestido Social",
  "data": "18 Mai 2025",
  "horario": "09:00",
  "status": "Em Produção"
}
```

## Observações

- O sistema usa persistência temporária em JSON para demonstrar a lógica funcional do backend.
- A estrutura foi organizada para facilitar a migração futura para banco de dados real.
- O dashboard visual do projeto permanece preservado e a integração com as novas áreas está funcional.
- Os testes automatizados validam a operação crítica da API.
