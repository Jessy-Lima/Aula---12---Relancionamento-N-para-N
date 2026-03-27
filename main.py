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

#Tabela Intermediaria
inscricoes = Table(
    "inscricoes", #nome da tabela
    Base.metadata,
    Column("aluno_id", Integer, ForeignKey("alunos.id"), primary_key=True),
    Column("curso_id", Integer, ForeignKey("cursos.id"), primary_key=True),
)

#Tabelas curso e aluno
class Aluno(Base):

    __tablename__ = "alunos"

    #Como criar um coluna
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    #Relacionamento
    cursos = relationship("Curso", secondary=inscricoes, back_populates="alunos")


    #Fução para imprimir
    def __repr__(self):
        return f"ID: {self.id} - NOME: {self.nome}"
    
class Curso(Base):
    __tablename__ = "cursos"

    #Como criar um coluna
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    #Relacionamento
    alunos = relationship("Aluno", secondary=inscricoes, back_populates="cursos")
    
    #Fução para imprimir
    def __repr__(self):
        return f"ID: {self.id} - NOME: {self.nome}"
    
#Conexão com db(tabela)
engine = create_engine("sqlite:///gestao_escolar.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

#Criar 
def cadastrar_curso():
    with Session() as session:
        try:
            #Criar o objeto curso
            nome_curso = input("Digite o nome do curso: ").capitalize()
            curso = Curso(nome=nome_curso)
            #Adicionar no banco
            session.add(curso)
            #Salvar
            session.commit()
            print(f"Curso {nome_curso} cadastrado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

# cadastrar_curso()

def cadastrar_aluno():
    with Session() as session:
        try:
            #Buscar o curso do aluno
            nome_curso = input("Digite o nome do curso para cadastrar o aluno: ").capitalize()
            curso = session.query(Curso).filter_by(nome=nome_curso).first()
            if curso == None:
                print(f"Nenhum curso encontrado com esse nome {nome_curso}")
                return
            else:
                nome_aluno = input("Digite o nome do aluno para cadastrar: ").capitalize()
                aluno = Aluno(nome=nome_aluno)
                aluno.cursos.append(curso)
                session.add(aluno)
                session.commit()
                print(f"Aluno cadastrado com sucesso!")

        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")
# cadastrar_aluno()

#Listar

#Atualizar

#Deletar