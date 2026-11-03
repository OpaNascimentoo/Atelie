from flask import Blueprint, jsonify, request

from backend.services.atelier_service import (
    create_pedido,
    delete_pedido,
    get_pedido_by_id,
    list_pedidos,
    update_pedido,
)

pedidos_bp = Blueprint("pedidos_bp", __name__)


@pedidos_bp.route("/api/pedidos", methods=["GET"])
def get_pedidos():
    return jsonify(list_pedidos()), 200


@pedidos_bp.route("/api/pedidos/<int:pedido_id>", methods=["GET"])
def get_pedido(pedido_id):
    pedido = get_pedido_by_id(pedido_id)
    if pedido is None:
        return jsonify({"error": "Pedido não encontrado."}), 404
    return jsonify(pedido), 200


@pedidos_bp.route("/api/pedidos", methods=["POST"])
def post_pedido():
    data = request.get_json(silent=True) or {}
    result, status_code = create_pedido(data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@pedidos_bp.route("/api/pedidos/<int:pedido_id>", methods=["PUT"])
def put_pedido(pedido_id):
    data = request.get_json(silent=True) or {}
    result, status_code = update_pedido(pedido_id, data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@pedidos_bp.route("/api/pedidos/<int:pedido_id>", methods=["DELETE"])
def delete_pedido_route(pedido_id):
    result, status_code = delete_pedido(pedido_id)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@pedidos_bp.route("/api/pedidos/<int:pedido_id>/status", methods=["PATCH"])
def patch_pedido_status(pedido_id):
    data = request.get_json(silent=True) or {}
    novo_status = data.get("status")
    if not novo_status:
        return jsonify({"error": "Status obrigatório."}), 400

    pedido = get_pedido_by_id(pedido_id)
    if pedido is None:
        return jsonify({"error": "Pedido não encontrado."}), 404

    if novo_status not in ["Agendado", "Em Produção", "Pronto para Prova", "Entregue"]:
        return jsonify({"error": "Status inválido para pedido."}), 400

    pedido["status"] = novo_status
    result, status_code = update_pedido(pedido_id, {"status": novo_status})
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code
