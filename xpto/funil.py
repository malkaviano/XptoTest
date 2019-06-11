# coding=utf-8

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base
from usuario import Usuario


class Funil(Base):
    __tablename__ = 'funil'

    user_id = Column(Integer, ForeignKey('usuarios.user_id'), primary_key=True)
    timestamp = Column(DateTime, primary_key=True)
    evento = Column(String)
    valor_simulado = Column(String)
    usuario = relationship(Usuario)

    def __repr__(self):
        return """<User(user_id='%s', timestamp='%s', evento='%s', valor_simulado='%s'>
            """ % (self.user_id, self.timestamp,
                   self.evento, self.valor_simulado)
