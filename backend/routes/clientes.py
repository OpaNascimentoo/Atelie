from flask import Blueprint, jsonify, request

from backend.services.atelier_service import (
    create_cliente,
    delete_cliente,
    get_cliente_by_id,
    list_clientes,
    update_cliente,
)

clientes_bp = Blueprint("clientes_bp", __name__)


@clientes_bp.route("/api/clientes", methods=["GET"])
def get_clientes():
    return jsonify(list_clientes()), 200


@clientes_bp.route("/api/clientes/<int:cliente_id>", methods=["GET"])
def get_cliente(cliente_id):
    cliente = get_cliente_by_id(cliente_id)
    if cliente is None:
        return jsonify({"error": "Cliente não encontrado."}), 404
    return jsonify(cliente), 200


@clientes_bp.route("/api/clientes", methods=["POST"])
def post_cliente():
    data = request.get_json(silent=True) or {}
    result, status_code = create_cliente(data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@clientes_bp.route("/api/clientes/<int:cliente_id>", methods=["PUT"])
def put_cliente(cliente_id):
    data = request.get_json(silent=True) or {}
    result, status_code = update_cliente(cliente_id, data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@clientes_bp.route("/api/clientes/<int:cliente_id>", methods=["DELETE"])
def delete_cliente_route(cliente_id):
    result, status_code = delete_cliente(cliente_id)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code
