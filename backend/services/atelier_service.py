from copy import deepcopy

from backend.data.mock_data import (
    CLIENTES_INICIAIS,
    DOACOES_INICIAIS,
    ENCOMENDAS_INICIAIS,
    PEDIDOS_INICIAIS,
    PRODUTOS_INICIAIS,
)
from backend.storage import load_store, save_store

STORE = load_store()
PEDIDOS = STORE["pedidos"]
CLIENTES = STORE["clientes"]
PRODUTOS = STORE["produtos"]
ENCOMENDAS = STORE["encomendas"]
DOACOES = STORE["doacoes"]

STATUSES_PEDIDO = ["Agendado", "Em Produção", "Pronto para Prova", "Entregue"]
VALID_STATUS = {
    "pedido": STATUSES_PEDIDO,
    "encomenda": [
        "Recebida",
        "Em análise",
        "Confirmada",
        "Em produção",
        "Pronta",
        "Entregue",
        "Cancelada",
        "Pendente",
    ],
    "doacao": ["Recebida", "Em avaliação", "Selecionada", "Em reaproveitamento", "Reaproveitada", "Recusada"],
}


def _persist_state():
    save_store({
        "pedidos": PEDIDOS,
        "clientes": CLIENTES,
        "produtos": PRODUTOS,
        "encomendas": ENCOMENDAS,
        "doacoes": DOACOES,
    })


def _error_response(message, status_code):
    return {"error": message}, status_code


def _require_fields(payload, fields):
    for field_name in fields:
        value = payload.get(field_name)
        if value is None or str(value).strip() == "":
            return False, f"Campo obrigatório ausente: {field_name}"
    return True, None


def _validate_status(status, tipo):
    return status in VALID_STATUS.get(tipo, [])


def list_pedidos():
    return deepcopy(PEDIDOS)


def get_pedido_by_id(pedido_id):
    for pedido in PEDIDOS:
        if pedido["id"] == pedido_id:
            return deepcopy(pedido)
    return None


def create_pedido(payload):
    ok, message = _require_fields(payload, ["cliente", "servico", "peca", "status"])
    if not ok:
        return _error_response(message, 400)

    if not _validate_status(payload["status"], "pedido"):
        return _error_response("Status inválido para pedido.", 400)

    pedido = {
        "id": (PEDIDOS[-1]["id"] + 1) if PEDIDOS else 1,
        "cliente": str(payload["cliente"]).strip(),
        "servico": str(payload["servico"]).strip(),
        "peca": str(payload["peca"]).strip(),
        "data": str(payload.get("data", "Sem data")).strip(),
        "horario": str(payload.get("horario", "--:--")).strip(),
        "status": str(payload["status"]).strip(),
    }
    PEDIDOS.append(pedido)
    _persist_state()
    return pedido, 201


def update_pedido(pedido_id, payload):
    pedido = get_pedido_by_id(pedido_id)
    if pedido is None:
        return _error_response("Pedido não encontrado.", 404)

    if "status" in payload and not _validate_status(payload["status"], "pedido"):
        return _error_response("Status inválido para pedido.", 400)

    for key, value in payload.items():
        if value is not None and key in pedido:
            pedido[key] = value

    for index, item in enumerate(PEDIDOS):
        if item["id"] == pedido_id:
            PEDIDOS[index] = pedido
            break
    _persist_state()
    return deepcopy(pedido), 200


def delete_pedido(pedido_id):
    for item in list(PEDIDOS):
        if item["id"] == pedido_id:
            PEDIDOS.remove(item)
            _persist_state()
            return {"message": "Pedido excluído com sucesso."}, 200
    return _error_response("Pedido não encontrado.", 404)


def list_clientes():
    return deepcopy(CLIENTES)


def get_cliente_by_id(cliente_id):
    for cliente in CLIENTES:
        if cliente["id"] == cliente_id:
            return deepcopy(cliente)
    return None


def create_cliente(payload):
    ok, message = _require_fields(payload, ["nome", "telefone", "email"])
    if not ok:
        return _error_response(message, 400)

    cliente = {
        "id": (CLIENTES[-1]["id"] + 1) if CLIENTES else 1,
        "nome": str(payload["nome"]).strip(),
        "telefone": str(payload["telefone"]).strip(),
        "email": str(payload["email"]).strip(),
        "endereco": str(payload.get("endereco", "")).strip(),
        "observacoes": str(payload.get("observacoes", "")).strip(),
        "pedidos": int(payload.get("pedidos", 0) or 0),
        "ultimo_atendimento": str(payload.get("ultimo_atendimento", "Sem registro")).strip(),
        "status": str(payload.get("status", "Ativa")).strip() or "Ativa",
    }
    CLIENTES.append(cliente)
    _persist_state()
    return cliente, 201


def update_cliente(cliente_id, payload):
    cliente = get_cliente_by_id(cliente_id)
    if cliente is None:
        return _error_response("Cliente não encontrado.", 404)
    for key, value in payload.items():
        if value is not None and key in cliente:
            cliente[key] = value
    for index, item in enumerate(CLIENTES):
        if item["id"] == cliente_id:
            CLIENTES[index] = cliente
            break
    _persist_state()
    return deepcopy(cliente), 200


def delete_cliente(cliente_id):
    for item in list(CLIENTES):
        if item["id"] == cliente_id:
            CLIENTES.remove(item)
            _persist_state()
            return {"message": "Cliente excluído com sucesso."}, 200
    return _error_response("Cliente não encontrado.", 404)


def list_produtos():
    return deepcopy(PRODUTOS)


def get_produto_by_id(produto_id):
    for produto in PRODUTOS:
        if produto["id"] == produto_id:
            return deepcopy(produto)
    return None


def create_produto(payload):
    ok, message = _require_fields(payload, ["nome", "categoria", "preco", "disponibilidade"])
    if not ok:
        return _error_response(message, 400)
    if float(payload["preco"]) < 0:
        return _error_response("Preço não pode ser negativo.", 400)

    produto = {
        "id": (PRODUTOS[-1]["id"] + 1) if PRODUTOS else 1,
        "nome": str(payload["nome"]).strip(),
        "descricao": str(payload.get("descricao", "")).strip(),
        "categoria": str(payload["categoria"]).strip(),
        "preco": float(payload["preco"]),
        "disponibilidade": str(payload["disponibilidade"]).strip(),
        "imagem": str(payload.get("imagem", "")).strip(),
        "material": str(payload.get("material", "Material premium")).strip(),
        "reaproveitado": bool(payload.get("reaproveitado", False)),
    }
    PRODUTOS.append(produto)
    _persist_state()
    return produto, 201


def update_produto(produto_id, payload):
    produto = get_produto_by_id(produto_id)
    if produto is None:
        return _error_response("Produto não encontrado.", 404)
    if "preco" in payload and float(payload["preco"]) < 0:
        return _error_response("Preço não pode ser negativo.", 400)
    for key, value in payload.items():
        if value is not None and key in produto:
            produto[key] = value
    for index, item in enumerate(PRODUTOS):
        if item["id"] == produto_id:
            PRODUTOS[index] = produto
            break
    _persist_state()
    return deepcopy(produto), 200


def delete_produto(produto_id):
    for item in list(PRODUTOS):
        if item["id"] == produto_id:
            PRODUTOS.remove(item)
            _persist_state()
            return {"message": "Produto excluído com sucesso."}, 200
    return _error_response("Produto não encontrado.", 404)


def list_encomendas():
    return deepcopy(ENCOMENDAS)


def get_encomenda_by_id(encomenda_id):
    for encomenda in ENCOMENDAS:
        if encomenda["id"] == encomenda_id:
            return deepcopy(encomenda)
    return None


def create_encomenda(payload):
    ok, message = _require_fields(payload, ["cliente", "produto", "quantidade", "status"])
    if not ok:
        return _error_response(message, 400)
    if int(payload["quantidade"]) <= 0:
        return _error_response("Quantidade deve ser maior que zero.", 400)
    if not _validate_status(payload["status"], "encomenda"):
        return _error_response("Status inválido para encomenda.", 400)

    quantidade = int(payload["quantidade"])
    valor_unitario = float(payload.get("valor_unitario", payload.get("valor", 0) or 0))
    valor_total = float(payload.get("valor_total", valor_unitario * quantidade or 0))

    encomenda = {
        "id": (ENCOMENDAS[-1]["id"] + 1) if ENCOMENDAS else 1,
        "numero": payload.get("numero") or f"# {str((ENCOMENDAS[-1]['id'] + 1) if ENCOMENDAS else 1).zfill(4)}",
        "cliente": str(payload["cliente"]).strip(),
        "produto": str(payload["produto"]).strip(),
        "quantidade": quantidade,
        "valor_unitario": valor_unitario,
        "valor_total": valor_total,
        "data": str(payload.get("data", "Sem data")).strip(),
        "status": str(payload["status"]).strip(),
        "observacao": str(payload.get("observacoes", payload.get("observacao", ""))).strip(),
        "observacoes": str(payload.get("observacoes", payload.get("observacao", ""))).strip(),
        "imagem": str(payload.get("imagem", "")).strip(),
    }
    ENCOMENDAS.append(encomenda)
    _persist_state()
    return encomenda, 201


def update_encomenda(encomenda_id, payload):
    encomenda = get_encomenda_by_id(encomenda_id)
    if encomenda is None:
        return _error_response("Encomenda não encontrada.", 404)
    if "status" in payload and not _validate_status(payload["status"], "encomenda"):
        return _error_response("Status inválido para encomenda.", 400)
    for key, value in payload.items():
        if value is not None and key in encomenda:
            encomenda[key] = value
    if "quantidade" in payload and "valor_unitario" in encomenda and encomenda["quantidade"] > 0:
        encomenda["valor_total"] = float(encomenda["valor_unitario"]) * float(encomenda["quantidade"])
    for index, item in enumerate(ENCOMENDAS):
        if item["id"] == encomenda_id:
            ENCOMENDAS[index] = encomenda
            break
    _persist_state()
    return deepcopy(encomenda), 200


def delete_encomenda(encomenda_id):
    for item in list(ENCOMENDAS):
        if item["id"] == encomenda_id:
            ENCOMENDAS.remove(item)
            _persist_state()
            return {"message": "Encomenda excluída com sucesso."}, 200
    return _error_response("Encomenda não encontrada.", 404)


def list_doacoes():
    return deepcopy(DOACOES)


def get_doacao_by_id(doacao_id):
    for doacao in DOACOES:
        if doacao["id"] == doacao_id:
            return deepcopy(doacao)
    return None


def create_doacao(payload):
    ok, message = _require_fields(payload, ["nome", "tipo_peca", "descricao", "estado_peca"])
    if not ok:
        return _error_response(message, 400)

    doacao = {
        "id": (DOACOES[-1]["id"] + 1) if DOACOES else 1,
        "nome": str(payload["nome"]).strip(),
        "tipo_peca": str(payload["tipo_peca"]).strip(),
        "descricao": str(payload["descricao"]).strip(),
        "estado_peca": str(payload["estado_peca"]).strip(),
        "data_doacao": str(payload.get("data_doacao", "Sem data")).strip(),
        "status": str(payload.get("status", "Recebida")).strip(),
        "observacao": str(payload.get("observacao", payload.get("observacoes", ""))).strip(),
        "observacoes": str(payload.get("observacoes", payload.get("observacao", ""))).strip(),
        "imagem": str(payload.get("imagem", "")).strip(),
    }
    DOACOES.append(doacao)
    _persist_state()
    return doacao, 201


def update_doacao(doacao_id, payload):
    doacao = get_doacao_by_id(doacao_id)
    if doacao is None:
        return _error_response("Doação não encontrada.", 404)
    for key, value in payload.items():
        if value is not None and key in doacao:
            doacao[key] = value
    for index, item in enumerate(DOACOES):
        if item["id"] == doacao_id:
            DOACOES[index] = doacao
            break
    _persist_state()
    return deepcopy(doacao), 200


def delete_doacao(doacao_id):
    for item in list(DOACOES):
        if item["id"] == doacao_id:
            DOACOES.remove(item)
            _persist_state()
            return {"message": "Doação excluída com sucesso."}, 200
    return _error_response("Doação não encontrada.", 404)
