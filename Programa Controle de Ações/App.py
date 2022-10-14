__license__ = 'GPL, GNU Public License'
__author__ = 'Rikerdaves'

from Banco import Banco
from User import Usuarios

from tkinter import *
from tkcalendar import Calendar, DateEntry

class Application:
    
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["pady"] = 15
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["pady"] = 15
        self.container11.pack()
        self.container12 = Frame(master)
        self.container12["pady"] = 15
        self.container12.pack()
        
        
        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()
        
        self.lblidusuario = Label(self.container2,
        text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)
        
        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)
        
        self.lbltaxa = Label(self.container3, text="Codigo da Ação:",
        font=self.fonte, width=14)
        self.lbltaxa.pack(side=LEFT)
        
        #Entrada do codigo de ação
        self.cod_ação = Entry(self.container3)
        self.cod_ação["width"] = 14
        self.cod_ação["font"] = self.fonte
        self.cod_ação.pack(padx = (0,100))
        
        self.lblval_unit = Label(self.container4, text="Valor Unit.: R$",
        font=self.fonte, width=12)
        self.lblval_unit.pack(side = LEFT)
        
        #Entrada do valor unitario
        self.val = Entry(self.container4)
        self.val["width"] = 8
        self.val["font"] = self.fonte
        self.val.pack(padx=(0,100))

        self.lblqt = Label(self.container5, text="Quant.:",
        font=self.fonte, width=10)
        self.lblqt.pack(side=LEFT)
        
        #Entrada do valor da quantidade
        self.qt = Entry(self.container5)
        self.qt["width"] = 8
        self.qt["font"] = self.fonte
        self.qt.pack(padx = (0,100))
        
        self.lbltaxa = Label(self.container6, text="Corretagem:",
        font=self.fonte, width=10)
        self.lbltaxa.pack(side=LEFT)
        
        #Entrada do valor da Taxa de corretagem
        self.corretagem = Entry(self.container6)
        self.corretagem["width"] = 8
        self.corretagem["font"] = self.fonte
        self.corretagem.pack(padx = (0,100))
        
        # Seleção da data na tela
        self.date = Label(self.container7, text='Data da Operação:')
        self.date ['font'] = ("Verdana", "9", "italic")
        self.date.pack(side=LEFT)
        self.data = DateEntry(self.container7, width= 16, background= "magenta3", date_pattern='dd-MM-yyyy', foreground= "white",bd=2)
        self.data.pack(pady=20)
        
        #Mostrar Resultado na tela
        self.resultado = Label(self.container9,text='Valor da Operação = R$', font=self.fonte, width=20).pack(side=LEFT)
        self.msg= Label(self.container9,width=16,font=self.fonte)
        self.msg.pack(side=LEFT)
        
        self.lblmsg = Label(self.container10, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
        
        #Botões de operações
        print_op=Button(self.container11, 
        font=self.fonte, text='Mostrar Operações', 
        command=table, width=16, background='#6c757d')
        print_op.pack(side=LEFT)
                
        compra=Button(self.container11, 
        font=self.fonte, text='Compra', 
        command=self.Op_compra, width=12, background='#6c757d')
        compra.pack(side=LEFT)
        
        venda=Button(self.container11, 
        font=self.fonte, text='Venda', 
        command=self.Op_venda, width=12, background='#6c757d')
        venda.pack(side=LEFT)
        
        #Botões CRUD
        self.bntInsert = Button (self.container12, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container12, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container12, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)
        
    def inserirUsuario(self):
        user = Usuarios()
        user.cod_acao = self.cod_ação.get()
        user.val = self.val.get()
        user.qt = self.qt.get()
        user.corretagem = self.corretagem.get()
        user.data = self.data.get()

        self.lblmsg["text"] = user.insertUser()
        
        self.txtidusuario.delete(0, END)
        self.cod_ação.delete(0, END)
        self.val.delete(0, END)
        self.qt.delete(0, END)
        self.corretagem.delete(0, END)
        self.data.delete(0, END)
        
    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.cod_acao = self.cod_ação.get()
        user.val = self.val.get()
        user.qt = self.qt.get()
        user.corretagem = self.corretagem.get()
        user.data = self.data.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidusuario.delete(0, END)
        self.cod_ação.delete(0, END)
        self.val.delete(0, END)
        self.qt.delete(0, END)
        self.corretagem.delete(0, END)
        self.data.delete(0, END)



    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidusuario.delete(0, END)
        self.cod_ação.delete(0, END)
        self.val.delete(0, END)
        self.qt.delete(0, END)
        self.corretagem.delete(0, END)
        self.data.delete(0, END)


    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.cod_ação.delete(0, END)
        self.cod_ação.insert(INSERT, user.cod_acao)

        self.val.delete(0, END)
        self.val.insert(INSERT,user.val)

        self.qt.delete(0, END)
        self.qt.insert(INSERT, user.qt)

        self.corretagem.delete(0, END)
        self.corretagem.insert(INSERT, user.corretagem)

        self.data.delete(0, END)
        self.data.insert(INSERT,user.data)
            

    # Calculo das operações
    def Op_compra(self):
        valor1 = self.val.get()
        valor2 = self.qt.get()
        valor3 = self.corretagem.get()
        taxa = 0.003
        valor1 = float(valor1)
        valor2 = int(valor2)
        valor3 = float(valor3)
        c = (valor1 * valor2) + taxa + valor3
        c = float(c)
        self.msg['text']=  '%.2f' %(c)
           
    def Op_venda(self):
        valor1 = self.val.get()
        valor2 = self.qt.get()
        valor3 = self.corretagem.get()
        taxa = 0.003
        valor1 = float(valor1)
        valor2 = int(valor2)
        valor3 = float(valor3)
        c = (valor1 * valor2) - taxa - valor3
        c = float(c)
        self.msg['text']= '%.2f' %(c)
        
import tkinter  as tk 
from tkinter import *
        
def table():
    import sqlite3
    my_conn = sqlite3.connect('banco.db')
        
    ##### tkinter window #####
    my_w = tk.Tk(className='Tabela de Operações')
    my_w.geometry("400x250")
        
    r_set=my_conn.execute('''SELECT * from usuarios LIMIT 0,10''');
    i=0 # row value inside the loop 
    for banco in r_set: 
        for j in range(len(banco)):
            e = Entry(my_w, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, banco[j])
        i=i+1
    my_w.mainloop() 
        

root = Tk(className=' Programa Controle de ações')
root.configure()
Application(root)
root.mainloop()



###### end of connection ####

##### tkinter window ######
 
 

      
      

