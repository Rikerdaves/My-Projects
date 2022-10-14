#importando SQlite
import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                    idusuario integer primary key autoincrement ,
                    cod_acao text,
                    val float,
                    qt integer,
                    corretagem float,
                    data text,
                    valor float,
                    tipo text)""")
        self.conexao.commit()
        c.close()