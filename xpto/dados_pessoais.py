# coding=utf-8

import json


class DadosPessoais(object):
    def __init__(self, genero, idade, estado_civil):
        self.genero = genero
        self.idade = idade
        self.estado_civil = estado_civil

    def normalisar_estado_civil(self):
        ec = self.estado_civil
        if ec == 'CASADO(A) COM BRASILEIRO(A) NATO(A)' or\
                ec == 'CASADO(A) COM BRASILEIRO(A) NATURALIZADO(A)' or\
                ec == 'UNIAO ESTAVEL':
            self.estado_civil = 'CASADO(A)'

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)

        return cls(**json_dict)
