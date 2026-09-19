# Persistência de Chamados

## Modelo simplificado do recurso

```
Chamado
- id: identificador único
- titulo: texto obrigatório
- descricao: texto obrigatório
- status: aberto | em_andamento | fechado
- criado_em: data e hora
```

## Script de criação da tabela

Localização: `database/001_criar_tabela_chamados.sql`

O script cria a tabela `chamados` com chave primária autoincremento, campos obrigatórios (`titulo`, `descricao`) e uma restrição (`CHECK`) que limita `status` aos valores `aberto`, `em_andamento` e `fechado`.

## Procedimento para preparar o banco

Não é necessário rodar o script manualmente. Ao iniciar a API (`uvicorn main:app --reload`), a função `inicializar_banco()` executa o script automaticamente e cria o arquivo `backend/chamados.db`, caso ele ainda não exista.

```
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Configuração de conexão

Banco: SQLite (arquivo local `backend/chamados.db`).
Não há variáveis de ambiente de conexão nesta versão, pois o SQLite não exige usuário, senha nem host — a conexão é feita diretamente com o arquivo local, sem credenciais.

## Endpoints implementados

| Método | URI | Comportamento |
|---|---|---|
| GET | `/` | Mensagem de status da API |
| GET | `/chamados` | Lista os chamados persistidos |
| POST | `/chamados` | Valida os dados, grava um chamado e retorna o recurso criado |
| GET | `/chamados/{id}` | Consulta um chamado pelo identificador |
| GET | `/chamados/status/{status}` | Lista chamados filtrados por status |

## Validação realizada

Criação de chamado sem o campo `titulo` retorna `422 Unprocessable Entity`, com o corpo indicando o campo ausente (validação automática do Pydantic).

## Erro tratado

Consulta a um `id` inexistente (ex: `GET /chamados/9999`) retorna `404 Not Found`, com a mensagem `"Chamado não encontrado"`.

## Decisões técnicas

- **SQLite em vez de um banco com servidor (Postgres/MySQL):** dispensa instalação e configuração de serviço externo, mantendo o ambiente simples para rodar localmente.
- **Camada de repositório separada (`repositorio_chamados.py`):** o `main.py` (rotas/controlador) não contém SQL nem lógica de acesso a dados; todas as queries ficam isoladas no repositório, usando parâmetros (`?`) em vez de concatenação de strings, evitando SQL injection.
- **`conexao.py` isolado:** concentra a criação da conexão e a inicialização do banco, separado da lógica de negócio.