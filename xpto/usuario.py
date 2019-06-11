from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    user_id = Column(Integer, primary_key=True)
    dados_pessoais = Column(String)
    nivel_de_risco = Column(Integer)
    objetivo = Column(String)
    perfil_de_risco = Column(String)
    fez_adicional = Column(Boolean)
    fez_resgate_parcial = Column(Boolean)
    fez_resgate_total = Column(Boolean)
    poupanca = Column(Float)
    renda_fixa = Column(Float)
    renda_variavel = Column(Float)

    def __repr__(self):
        return """<User(user_id='%s', dados_pessoais='%s', nivel_de_risco='%s',
            objetivo='%s', perfil_de_risco='%s', fez_adicional='%s',
            fez_resgate_parcial='%s', fez_resgate_total='%s', poupanca='%s',
            renda_fixa='%s', renda_variavel='%s'>
            """ % (self.user_id, self.dados_pessoais, self.nivel_de_risco,
                   self.objetivo, self.perfil_de_risco, self.fez_adicional,
                   self.fez_resgate_parcial, self.fez_resgate_total,
                   self.poupanca, self.renda_fixa, self.renda_variavel
                   )
