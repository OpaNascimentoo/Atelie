import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from flask import Flask, jsonify, send_from_directory

from backend.routes.clientes import clientes_bp
from backend.routes.doacoes import doacoes_bp
from backend.routes.encomendas import encomendas_bp
from backend.routes.pedidos import pedidos_bp
from backend.routes.vitrine import vitrine_bp

BASE_DIR = Path(__file__).resolve().parent.parent


def create_app():
    app = Flask(__name__)

    app.register_blueprint(pedidos_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(vitrine_bp)
    app.register_blueprint(encomendas_bp)
    app.register_blueprint(doacoes_bp)

    @app.route("/")
    def index():
        return send_from_directory(str(BASE_DIR), "index.html.html")

    @app.route("/api/health")
    def health():
        return jsonify({"status": "ok", "message": "Ateliê Bella API funcionando."}), 200

    @app.route("/assets/<path:filename>")
    def serve_assets(filename):
        return send_from_directory(str(ROOT_DIR / "assets"), filename)

    @app.route("/imagens/<path:filename>")
    def serve_imagens(filename):
        return send_from_directory(str(ROOT_DIR / "imagens"), filename)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
