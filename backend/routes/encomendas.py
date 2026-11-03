from flask import Blueprint, jsonify, request

from backend.services.atelier_service import (
    create_encomenda,
    delete_encomenda,
    get_encomenda_by_id,
    list_encomendas,
    update_encomenda,
)

encomendas_bp = Blueprint("encomendas_bp", __name__)


@encomendas_bp.route("/api/encomendas", methods=["GET"])
def get_encomendas():
    return jsonify(list_encomendas()), 200


@encomendas_bp.route("/api/encomendas/<int:encomenda_id>", methods=["GET"])
def get_encomenda(encomenda_id):
    encomenda = get_encomenda_by_id(encomenda_id)
    if encomenda is None:
        return jsonify({"error": "Encomenda não encontrada."}), 404
    return jsonify(encomenda), 200


@encomendas_bp.route("/api/encomendas", methods=["POST"])
def post_encomenda():
    data = request.get_json(silent=True) or {}
    result, status_code = create_encomenda(data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@encomendas_bp.route("/api/encomendas/<int:encomenda_id>", methods=["PUT"])
def put_encomenda(encomenda_id):
    data = request.get_json(silent=True) or {}
    result, status_code = update_encomenda(encomenda_id, data)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code


@encomendas_bp.route("/api/encomendas/<int:encomenda_id>", methods=["DELETE"])
def delete_encomenda_route(encomenda_id):
    result, status_code = delete_encomenda(encomenda_id)
    if status_code >= 400:
        return jsonify(result), status_code
    return jsonify(result), status_code
