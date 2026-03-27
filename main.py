#Relacionamentos Muitos para muitos (N:N)

# Estudantes se inscrevem em cursos.
# um estydante pode fazer vários cursos
# um curso pode ter vários estudantes

# Forma simples:
# A relação não precisa guardar dados extras
# Só fazer o relacionamento

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

#Tabelas curso e aluno
class Aluno(Base):

    __tablename__ = "alunos"

    #Como criar um coluna
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    #Fução para imprimir
    def __repr__(self):
        return f"ID: {self.id} - NOME: {self.nome}"
    
    