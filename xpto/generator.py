# coding=utf-8

# Código usado apenas para gerar sample data

from database import create_session
from datetime import datetime, timedelta
from random import randint, uniform, getrandbits
from usuario import Usuario
from funil import Funil
from values import DB_PATH
import uuid


def rand_float(min, max):
    return round(uniform(min, max), 2)


def rand_int(min, max):
    return randint(min, max)


def rand_str():
    return str(uuid.uuid4())


def rand_boolean():
    return bool(getrandbits(1))


def rand_profile():
    p = ['CONSERVADOR', 'MODERADO', 'AGRESSIVO']

    return p[rand_int(0, 2)]


def rand_gender():
    return 'M' if rand_boolean() else 'F'


def rand_marital():
    m = [
        "CASADO(A) COM BRASILEIRO(A) NATO(A)",
        "CASADO(A) COM BRASILEIRO(A) NATURALIZADO(A)",
        "UNIAO ESTAVEL",
        "CASADO(A)",
        "DIVORCIADO(A)",
        "SOLTEIRO(A)"
        ]

    return m[rand_int(0, 5)]


def rand_json():
    m = rand_marital()
    age = rand_int(18, 80)
    g = rand_gender()

    return '{' + f'"genero":"{g}","idade":{age},"estado_civil":"{m}"' + '}'


def generate_data():
    Session = create_session(DB_PATH)

    session = Session()

    u = []

    for i in range(1, 10000):
        u.append(Usuario(
            user_id=i,
            dados_pessoais=rand_json(),
            nivel_de_risco=rand_int(1, 10),
            objetivo=rand_str(),
            perfil_de_risco=rand_profile(),
            fez_adicional=rand_boolean(),
            fez_resgate_parcial=rand_boolean(),
            fez_resgate_total=rand_boolean(),
            poupanca=rand_float(1000, 100000),
            renda_fixa=rand_float(1000, 100000),
            renda_variavel=rand_float(1000, 100000),
        ))

    session.add_all(u)

    session.commit()

    f = []

    for i in range(1, 10000):
        if rand_int(1, 10) < 7:
            for j in range(rand_int(1, 20)):
                f.append(Funil(
                    user_id=i,
                    timestamp=(
                        datetime.now() - timedelta(seconds=rand_int(1, 100000))
                        ),
                    evento=rand_str(),
                    valor_simulado=rand_float(1000, 10000),
                    usuario=u[i - 1]
                ))

    session.add_all(f)

    session.commit()


generate_data()
