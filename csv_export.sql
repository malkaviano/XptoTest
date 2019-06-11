.headers on
.mode csv
.output xpto.csv
WITH RECURSIVE split(id, json_value, rest) AS (
  SELECT user_id, '', dados_pessoais || ',' FROM (
    select user_id, replace(replace(replace(dados_pessoais, '"', ''), '}', ''), '{', '') as dados_pessoais from usuarios
  )
   UNION ALL
  SELECT id,
         substr(rest, 0, instr(rest, ',')),
         substr(rest, instr(rest, ',')+1)
    FROM split
   WHERE rest <> '')

SELECT u.user_id,
    trim(CASE WHEN INSTR(s1.json_value, 'genero') > 0 THEN replace(s1.json_value, 'genero:', '') END) as genero,
    trim(CASE WHEN INSTR(s2.json_value, 'idade') > 0 THEN replace(s2.json_value, 'idade:', '') END) as idade,
    trim(CASE WHEN INSTR(s3.json_value, 'estado_civil') > 0 THEN
        replace(
            replace(
                replace(
                    replace(s3.json_value, 'estado_civil:', ''),
                    'UNIAO ESTAVEL',
                    'CASADO(A)'
                ),
                'CASADO(A) COM BRASILEIRO(A) NATO(A)',
                'CASADO(A)'
            ),
            'CASADO(A) COM BRASILEIRO(A) NATURALIZADO(A)',
            'CASADO(A)'
        )
    END) as estado_civil,
    u.nivel_de_risco,
    u.objetivo,
    u.perfil_de_risco,
    (select strftime('%Y-%m', min(timestamp)) from funil as f where f.user_id = u.user_id) as homepage,
    (
        select valor_simulado
        from funil as f
        where f.user_id = u.user_id
        group by f.user_id
        having max(timestamp)
    ) as valor_simulado,
    (u.poupanca + u.renda_fixa + u.renda_variavel) as investimentos_externos
  FROM split as s1
  inner join split as s2
  on s1.id = s2.id
  inner join split as s3
  on s1.id = s3.id
  inner join usuarios as u
  on s1.id = u.user_id
 WHERE genero <> '' and
        idade <> '' and
        estado_civil <> '' and
        s1.json_value <> s2.json_value and
        s1.json_value <> s3.json_value and
        s2.json_value <> s3.json_value and
        u.fez_adicional = 1 and not (u.fez_resgate_parcial and u.fez_resgate_total)
 ;