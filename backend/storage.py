import json
from copy import deepcopy
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT_DIR / "backend" / "data" / "store.json"


def _initial_store():
    from backend.data.mock_data import (
        CLIENTES_INICIAIS,
        DOACOES_INICIAIS,
        ENCOMENDAS_INICIAIS,
        PEDIDOS_INICIAIS,
        PRODUTOS_INICIAIS,
    )

    return {
        "pedidos": deepcopy(PEDIDOS_INICIAIS),
        "clientes": deepcopy(CLIENTES_INICIAIS),
        "produtos": deepcopy(PRODUTOS_INICIAIS),
        "encomendas": deepcopy(ENCOMENDAS_INICIAIS),
        "doacoes": deepcopy(DOACOES_INICIAIS),
    }


def load_store():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        save_store(_initial_store())
        return _initial_store()

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return {
            "pedidos": data.get("pedidos", _initial_store()["pedidos"]),
            "clientes": data.get("clientes", _initial_store()["clientes"]),
            "produtos": data.get("produtos", _initial_store()["produtos"]),
            "encomendas": data.get("encomendas", _initial_store()["encomendas"]),
            "doacoes": data.get("doacoes", _initial_store()["doacoes"]),
        }
    except (json.JSONDecodeError, OSError):
        save_store(_initial_store())
        return _initial_store()


def save_store(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
