from Banco import Banco

class Usuarios(object):
    def __init__(self, idusuario = 0, cod_acao = "", val = "", qt = "", corretagem = "", data = ""):
        self.info = {}
        self.idusuario = idusuario
        self.cod_acao = cod_acao
        self.val = val
        self.qt = qt
        self.corretagem = corretagem
        self.data = data

    def insertUser(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into usuarios (cod_acao, val, qt, corretagem, data) values ('" + self.cod_acao + "', '" +
            self.val + "', '" + self.qt + "', '" +
            self.corretagem + "', '" + self.data + "' )")
            banco.conexao.commit()
            c.close()
            return "Operação cadastrada com sucesso!"
        except:
            return "Ocorreu um erro na inserção da operação"

    def updateUser(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update usuarios set cod_acao = '" + self.cod_acao + "', val = '" + 
            self.val + "', qt = '" + self.qt +
            "', corretagem = '" + self.corretagem + "', data = '" + self.data +
            "' where idusuario = " + self.idusuario + " ")
            banco.conexao.commit()
            c.close()

            return "Operação atualizada com sucesso!"
        except:
            return "Ocorreu um erro na alteração da Operação"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Operação excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão da operação"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = " + idusuario + "  ")

            for linha in c:
                self.idusuario = linha[0]
                self.cod_acao = linha[1]
                self.val = linha[2]
                self.qt = linha[3]
                self.corretagem = linha[4]
                self.data = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da operação"