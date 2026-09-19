from conexao import obter_conexao


def inserir_chamado(titulo: str, descricao: str, status: str = "aberto") -> dict:
    with obter_conexao() as conexao:
        cursor = conexao.execute(
            "INSERT INTO chamados (titulo, descricao, status) VALUES (?, ?, ?)",
            (titulo, descricao, status),
        )
        conexao.commit()
        return buscar_chamado_por_id(cursor.lastrowid)


def listar_chamados() -> list[dict]:
    with obter_conexao() as conexao:
        linhas = conexao.execute("SELECT * FROM chamados").fetchall()
        return [dict(linha) for linha in linhas]


def buscar_chamado_por_id(chamado_id: int) -> dict | None:
    with obter_conexao() as conexao:
        linha = conexao.execute(
            "SELECT * FROM chamados WHERE id = ?", (chamado_id,)
        ).fetchone()
        return dict(linha) if linha else None


def listar_por_status(status_chamado: str) -> list[dict]:
    with obter_conexao() as conexao:
        linhas = conexao.execute(
            "SELECT * FROM chamados WHERE status = ?", (status_chamado,)
        ).fetchall()
        return [dict(linha) for linha in linhas]