# coding=utf-8

import csv
from sqlalchemy import and_
from usuario import Usuario
from funil import Funil
from sqlalchemy import func
from dados_pessoais import DadosPessoais
from values import CSV_PATH


class CSVPipeline:
    def __init__(self, Session):
        self.Session = Session

    def generate_csv(self):
        # may suffer from out of memory, but was not specified in the exercise
        result = self.__data()

        self.__write_csv(result)

    def __data(self):
        session = self.Session()

        data = []

        for u in session.query(Usuario).\
                filter(Usuario.user_id == Funil.user_id).\
                filter(Usuario.fez_adicional).\
                filter(~and_(
                    Usuario.fez_resgate_parcial,
                    Usuario.fez_resgate_total)
                ).\
                all():

            dados_pessoais = DadosPessoais.from_json(u.dados_pessoais)
            dados_pessoais.normalisar_estado_civil()

            first_visit = session.query(func.min(Funil.timestamp)).\
                filter(Funil.user_id == u.user_id).\
                scalar()

            homepage = first_visit.strftime('%Y-%m')

            valor_simulado = session.query(Funil.valor_simulado).\
                filter(Funil.user_id == u.user_id).\
                group_by(Funil.user_id).\
                having(func.max(Funil.timestamp)).\
                scalar()

            investimentos_externos = u.poupanca + u.renda_fixa +\
                u.renda_variavel

            data.append((
                u.user_id, dados_pessoais.genero,
                dados_pessoais.estado_civil, dados_pessoais.idade,
                u.nivel_de_risco, u.objetivo, u.perfil_de_risco,
                homepage, valor_simulado, investimentos_externos
            ))

        session.close()

        return data

    def __write_csv(self, data):
        with open(CSV_PATH, mode='w') as csv_file:
            writer = csv.writer(
                csv_file, delimiter=',', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)

            writer.writerow([
                'user_id', 'genero', 'estado_civil', 'idade',
                'nivel_de_risco', 'objetivo', 'perfil_de_risco',
                'homepage', 'valor_simulado', 'investimentos_externos'
            ])

            writer.writerows(data)
