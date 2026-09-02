# Planejamento Inicial — Sistema de Gestão de Chamados

## 1. Descrição do problema e do domínio

A empresa de suporte técnico hoje controla as solicitações de clientes por meio de planilhas e mensagens dispersas, o que dificulta localizar chamados, acompanhar o andamento dos atendimentos e manter um histórico confiável. A nova aplicação deve centralizar o registro e o acompanhamento de chamados, permitindo que clientes abram solicitações e que a equipe de suporte as consulte, atualize e encerre. O domínio atendido é o de **suporte técnico / atendimento ao cliente (help desk)**.

## 2. Escopo inicial

**Incluído na primeira versão:**
- Cadastro de chamados
- Consulta de chamados
- Atualização de status
- Encerramento de chamados

**Fora do escopo inicial (evolução futura):**
- Envio de notificações automáticas (e-mail/push) sobre mudanças de status
- Anexos de arquivos nos chamados
- Relatórios e painéis de indicadores

## 3. Pessoas usuárias

| Pessoa usuária | Objetivo principal |
|---|---|
| Pessoa cliente | Registrar e acompanhar um chamado |
| Pessoa atendente | Consultar, atualizar e encerrar chamados |

## 4. Requisitos funcionais

1. O sistema deve permitir que uma pessoa cliente registre um chamado com título e descrição.
2. O sistema deve permitir que uma pessoa cliente consulte o status dos seus próprios chamados.
3. O sistema deve permitir que uma pessoa atendente consulte os chamados abertos.
4. O sistema deve permitir que uma pessoa atendente altere o status de um chamado.
5. O sistema deve permitir que uma pessoa atendente encerre um chamado resolvido.

## 5. Recursos principais do sistema

| Recurso | Possíveis informações |
|---|---|
| Chamado | identificador, título, descrição, status, data de abertura |
| Cliente | identificador, nome, contato |
| Atendente | identificador, nome |
| Categoria | identificador, nome |

## 6. Fluxo prioritário — Registrar chamado

1. A pessoa cliente acessa a tela de abertura de chamado.
2. A pessoa informa título e descrição do problema.
3. A interface envia as informações para a API.
4. O back-end valida os dados recebidos.
5. O back-end cria o registro do chamado com status "aberto".
6. O banco de dados armazena o registro.
7. A aplicação retorna a confirmação à interface.
8. A interface informa à pessoa cliente que o chamado foi registrado com sucesso.

## 7. Diagrama arquitetural (simplificado)

```
Pessoa cliente / atendente
        ↓
  Interface web (front-end)
        ↓  ↑
        API
        ↓  ↑
Back-end e regras de negócio
        ↓  ↑
    Banco de dados

  (futuro) Serviço de notificações → conectado ao back-end
```

**Papel de cada componente:**
- **Interface web:** coleta os dados da pessoa usuária e exibe o retorno da API.
- **API:** ponto único de entrada, recebe as requisições da interface e as encaminha ao back-end.
- **Back-end:** aplica as regras de negócio (validação de dados, transições de status permitidas).
- **Banco de dados:** armazena de forma persistente os chamados, clientes, atendentes e categorias.

**Discussão:**
- A interface apenas coleta e exibe dados; não decide regras.
- A regra de "quais transições de status são permitidas" deve ficar no back-end.
- Os chamados são armazenados no banco de dados.
- Se as responsabilidades estiverem bem separadas, o componente de interface (front-end) é o que pode ser substituído com menor impacto, pois a API e o back-end não dependem de sua implementação específica.

## 8. Organização inicial do repositório

```
projeto-chamados/
├── README.md
├── docs/
│   ├── planejamento-semana-1.md
│   └── diagrama-arquitetura.md
├── frontend/
├── backend/
└── database/
```

**README.md (sugestão de conteúdo):**
> **Projeto:** Sistema de Gestão de Chamados
> **Objetivo:** Centralizar o registro, o acompanhamento e o encerramento de chamados de suporte técnico, substituindo o controle atual por planilhas e mensagens dispersas.

## 9. Registro de decisões e dúvidas

**Decisões:**
- O fluxo prioritário da primeira versão será "Registrar chamado".
- Notificações, anexos e relatórios ficam fora do escopo inicial.

**Dúvida em aberto:**
- Uma pessoa atendente poderá reabrir um chamado já encerrado, ou isso exigirá a abertura de um novo chamado?
