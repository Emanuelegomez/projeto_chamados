# Contrato inicial — API de Chamados

## Recurso
- Nome: `chamados`
- Finalidade: registrar e acompanhar solicitações de suporte.

## Formato de dados
- Requisições e respostas: JSON

## Atributos

| Campo | Tipo | Obrigatório na criação? | Descrição |
|---|---|---|---|
| id | número inteiro | Não | Identificador do chamado |
| titulo | texto | Sim | Resumo do problema |
| descricao | texto | Sim | Detalhamento do problema |
| prioridade | texto | Sim | Nível de prioridade (`baixa`, `media`, `alta`) |
| status | texto | Não | Situação do chamado (padrão: `aberto`) |

## Endpoints

| Operação | Método | URI | Parâmetros | Status previstos |
|---|---|---|---|---|
| Listar chamados | GET | `/chamados` | Opcional: `status` (query string) | 200 |
| Consultar chamado | GET | `/chamados/{id}` | `id` na URI | 200, 404 |
| Criar chamado | POST | `/chamados` | Corpo JSON | 201, 400 |
| Atualizar chamado | PATCH | `/chamados/{id}` | `id` na URI + corpo JSON | 200, 400, 404 |
| Remover chamado | DELETE | `/chamados/{id}` | `id` na URI | 204, 404 |

## Exemplo — criação bem-sucedida

**Requisição:**
```
POST /chamados
Content-Type: application/json

{
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "alta"
}
```

**Resposta:**
```
HTTP/1.1 201 Created
Content-Type: application/json
Location: /chamados/42

{
  "id": 42,
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "alta",
  "status": "aberto"
}
```

## Exemplo — erro 400 (dado inválido)

Criação sem o campo `titulo`:
```json
{
  "erro": "Dado inválido",
  "detalhes": [
    {
      "campo": "titulo",
      "mensagem": "O título é obrigatório."
    }
  ]
}
```

## Exemplo — erro 404 (recurso inexistente)

Consulta de `/chamados/9999`, quando o chamado não existe.

## Decisões e dúvidas pendentes

- Decisão: `PATCH` foi escolhido em vez de `PUT` para atualização, pois a alteração normalmente afeta apenas alguns campos (ex: só o status).
- Dúvida: uma pessoa atendente poderá reabrir um chamado já encerrado, ou isso exigirá a abertura de um novo chamado?
