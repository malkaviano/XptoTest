--SQLite version 3.8.7.1
PRAGMA foreign_keys = ON;

drop table funil;

drop table usuarios;

create table if not exists usuarios(
    user_id int primary key,
    dados_pessoais text,
    nivel_de_risco int,
    objetivo text,
    perfil_de_risco text,
    fez_adicional boolean,
    fez_resgate_parcial boolean,
    fez_resgate_total boolean,
    poupanca real,
    renda_fixa real,
    renda_variavel real
);

create table if not exists funil(
    user_id int,
    timestamp datetime,
    evento text,
    valor_simulado real,
    PRIMARY KEY (user_id, timestamp),
    FOREIGN KEY(user_id) REFERENCES usuarios(user_id)
);