from flask import Blueprint, jsonify, request

from backend.services.atelier_service import (
    create_produto,
    delete_produto,
    get_produto_by_id,
    list_produtos,
    update_produto,
)

vitrine_bp = Blueprint("vitrine_bp", __name__)


@vitrine_bp.route("/api/produtos", methods=["GET"])
def get_produtos():
    return jsonify(list_produtos()), 200


@vitrine_bp.route("/api/produtos/<int:produto_id>", methods=["GET"])
def get_produto(produto_id):
    produto = get_produto_by_id(produto_id)
    if produto is None:
        return jsonify({"error": "Produto não encontrado."}), 404
    return jsonify(produto), 200


@vitrine_bp.route("/api/produtos", methods=["POST"])
def post_produto():
    data = request.get_json(silent=True) or {}
    result, status_code = create_produto(data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@vitrine_bp.route("/api/produtos/<int:produto_id>", methods=["PUT"])
def put_produto(produto_id):
    data = request.get_json(silent=True) or {}
    result, status_code = update_produto(produto_id, data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@vitrine_bp.route("/api/produtos/<int:produto_id>", methods=["DELETE"])
def delete_produto_route(produto_id):
    result, status_code = delete_produto(produto_id)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code
