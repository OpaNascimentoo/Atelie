from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Pedido:
    id: int
    cliente: str
    servico: str
    peca: str
    data: str
    horario: str
    status: str


@dataclass
class Cliente:
    id: int
    nome: str
    telefone: str
    email: str
    endereco: str = ""


@dataclass
class Produto:
    id: int
    nome: str
    descricao: str
    categoria: str
    preco: float
    disponibilidade: str
    imagem: str = ""


@dataclass
class Encomenda:
    id: int
    cliente: str
    produto: str
    quantidade: int
    data: str
    status: str
    observacoes: str = ""


@dataclass
class Doacao:
    id: int
    nome: str
    tipo_peca: str
    descricao: str
    estado_peca: str
    data_doacao: str
    observacoes: str = ""
