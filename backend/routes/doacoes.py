from flask import Blueprint, jsonify, request

from backend.services.atelier_service import (
    create_doacao,
    delete_doacao,
    get_doacao_by_id,
    list_doacoes,
    update_doacao,
)

doacoes_bp = Blueprint("doacoes_bp", __name__)


@doacoes_bp.route("/api/doacoes", methods=["GET"])
def get_doacoes():
    return jsonify(list_doacoes()), 200


@doacoes_bp.route("/api/doacoes/<int:doacao_id>", methods=["GET"])
def get_doacao(doacao_id):
    doacao = get_doacao_by_id(doacao_id)
    if doacao is None:
        return jsonify({"error": "Doação não encontrada."}), 404
    return jsonify(doacao), 200


@doacoes_bp.route("/api/doacoes", methods=["POST"])
def post_doacao():
    data = request.get_json(silent=True) or {}
    result, status_code = create_doacao(data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@doacoes_bp.route("/api/doacoes/<int:doacao_id>", methods=["PUT"])
def put_doacao(doacao_id):
    data = request.get_json(silent=True) or {}
    result, status_code = update_doacao(doacao_id, data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@doacoes_bp.route("/api/doacoes/<int:doacao_id>", methods=["DELETE"])
def delete_doacao_route(doacao_id):
    result, status_code = delete_doacao(doacao_id)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code
