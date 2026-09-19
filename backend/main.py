from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, field_validator

import repositorio_chamados as repositorio
from conexao import inicializar_banco

app = FastAPI(title="API de Chamados")

STATUS_VALIDOS = {"aberto", "em_andamento", "fechado"}


@app.on_event("startup")
def preparar_banco():
    inicializar_banco()


class ChamadoEntrada(BaseModel):
    titulo: str
    descricao: str
    status: str = "aberto"

    @field_validator("status")
    @classmethod
    def validar_status(cls, valor: str) -> str:
        if valor not in STATUS_VALIDOS:
            raise ValueError(f"status deve ser um de: {', '.join(STATUS_VALIDOS)}")
        return valor


@app.get("/")
def inicio():
    return {"mensagem": "API de Chamados ativa"}


@app.get("/chamados")
def listar_chamados():
    return repositorio.listar_chamados()


@app.post("/chamados", status_code=status.HTTP_201_CREATED)
def criar_chamado(dados: ChamadoEntrada):
    return repositorio.inserir_chamado(
        titulo=dados.titulo,
        descricao=dados.descricao,
        status=dados.status,
    )


@app.get("/chamados/{chamado_id}")
def buscar_chamado(chamado_id: int):
    chamado = repositorio.buscar_chamado_por_id(chamado_id)
    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    return chamado


@app.get("/chamados/status/{status_chamado}")
def buscar_por_status(status_chamado: str):
    return repositorio.listar_por_status(status_chamado)