import sqlite3
from pathlib import Path

CAMINHO_BANCO = Path(__file__).parent / "chamados.db"
CAMINHO_SCRIPT = Path(__file__).parent.parent / "database" / "001_criar_tabela_chamados.sql"


def obter_conexao():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco():
    with obter_conexao() as conexao:
        with open(CAMINHO_SCRIPT, "r", encoding="utf-8") as arquivo:
            conexao.executescript(arquivo.read())