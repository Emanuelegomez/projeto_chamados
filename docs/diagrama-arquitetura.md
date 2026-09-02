# Diagrama Arquitetural — Sistema de Chamados

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

## Papel de cada componente

- **Interface web:** coleta os dados da pessoa usuária e exibe o retorno da API.
- **API:** ponto único de entrada, recebe as requisições da interface e as encaminha ao back-end.
- **Back-end:** aplica as regras de negócio (validação de dados, transições de status permitidas).
- **Banco de dados:** armazena de forma persistente os chamados, clientes, atendentes e categorias.

## Discussão

- A interface apenas coleta e exibe dados; não decide regras.
- A regra de "quais transições de status são permitidas" deve ficar no back-end.
- Os chamados são armazenados no banco de dados.
- Se as responsabilidades estiverem bem separadas, o componente de interface (front-end) é o que pode ser substituído com menor impacto, pois a API e o back-end não dependem de sua implementação específica.

## Evolução futura

Um bloco de "Serviço de notificações" pode ser conectado ao back-end como evolução futura. Ele não faz parte do escopo obrigatório da primeira versão.
