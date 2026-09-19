-- database/001_criar_tabela_chamados.sql
-- Cria a tabela de persistência do recurso "chamados"

CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(120) NOT NULL,
    descricao TEXT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'aberto',
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chamados_status_valido
        CHECK (status IN ('aberto', 'em_andamento', 'fechado'))
);
