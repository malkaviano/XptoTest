### Esse projeto é a solução proposta ao exercício enviado.

**Arquivos notórios:**
- sql_schemas: contém o schema das tabelas geradas;
- csv_export: script SQL com a solução SQL solicitada (só rodar o script dentro do sqlite);
- xpto_csv: sample do csv gerado pelo código;
- DATA_XPTO.db: um banco de dados sample com 10 mil usuários e 60K+ de funil;

**Pasta xpto: contém a solução Python. O código depende apenas do SQLAlquemy, como solicitado apenas Python foi usado.**

O código aceita path para outro banco como argumento na linha de comando.

O CSV sempre é gerado na pasta root do projeto.

Nota: Deveria ter usado Pandas.