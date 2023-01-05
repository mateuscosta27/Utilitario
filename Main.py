import sys
from View.Chamado import *
from configs.config import *
from configs.Transact import *
from View.Cadastro import *
from View.Principal import *
from View.MessageBox import *

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sqlite3


class TelaChamado(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaChamado()
        self.ui.setupUi(self)


        self.config = Conf()
        self.ui.lb_commom.setText(f'Todos os direitos reservados | Versão - {self.config.version} | {self.config.data}')
        self.ui.btn_end.clicked.connect(self.expand_window)

    def expand_window(self):
        self.resize(1275,560)
    
 

class MessageBox(QMainWindow):
    def __init__(self, mensagem):
        super().__init__()
        self.ui = Ui_MessageBox()
        self.ui.setupUi(self)

        ###formatação###
        self.mensagem = mensagem
        self.ui.lb_message.setText(self.mensagem)
        self.ui.lb_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        ##botões##
        self.ui.btn_cancel.clicked.connect(self.close_window)


    def close_window(self):
        self.close()    

    def disable_button_yes(self):
        self.ui.btn_yes.setVisible(False)
        
        
  
    
class TelaCadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaCadastro()
        self.ui.setupUi(self)


        self.config = Conf()
        self.ui.lb_commom.setText(f'Todos os direitos reservados | Versão - {self.config.version} | {self.config.data}')

        ###botoes###

        self.ui.btn_add.clicked.connect(self.add_employee)
        self.ui.btn_remove.clicked.connect(self.message_exists)

    

    def connect_db(self):
        ###conexão com o banco de dados###
        init = open('connectDB.txt','r')
        directoryDB = init.read()
        self.conn = sqlite3.connect(directoryDB)


    ###retorna para a tela principal###
    def closeEvent(self, event):
        self.return_origem = TelaPrincipal()
        self.return_origem.show()
        event.accept()


    def add_employee(self):

        nome = self.ui.le_name.text()
        setor = self.ui.cbb_sector.currentText()
        ramal_in = self.ui.le_branchIn.text()
        ramal_ex = self.ui.le_branchEx.text()
        mask = '(),- '
        celular = self.ui.le_cellPhone.text()
        for i in mask:
            celular = celular.replace(i,'')

        
        cursor = self.conn.cursor()
        sql_exists = (F"""
            select
                EXISTS (
                SELECT
                    1
                FROM
                    tb_funcionario tf
                WHERE 
                    Nome = "{nome}"
                    AND setor = "{setor}"
                    AND ramal_interno = {ramal_in} )
        """)

        cursor.execute(sql_exists)
        result = cursor.fetchall()
        exist = result[0][0]
        if exist == 0:
            sql_insert = f"""

            INSERT INTO tb_funcionario(Nome,setor, ramal_interno,ramal_externo, celular,status) values ('{nome}', '{setor}',{ramal_in},{ramal_ex},'{celular}','Livre')
            """
            cursor.execute(sql_insert)
            self.conn.commit()
            self.message_sucess_add(mess='Funcionario cadastrado com sucesso!')
            
        else:
            self.message_exists(mess=f"Ja existe um cadastro com estes dados\n Nome: {nome}, Ramal: {ramal_in}")
            print("Existe")       

    def message_sucess_add(self, mess):
        self.mess = mess
        mensagem = MessageBox(self.mess)
        mensagem.ui.btn_yes.setText("Ok")
        mensagem.ui.btn_cancel.setVisible(False)
        mensagem.ui.btn_yes.setGeometry(250,157,100,45)
        mensagem.show()
        mensagem.exec()




    def message_exists(self,mess):
        self.mess = mess
        mensagem = MessageBox(self.mess)
        mensagem.disable_button_yes()
        mensagem.ui.btn_cancel.setGeometry(250,157,100,45)
        mensagem.show()
        mensagem.exec()


        
        

        




class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        
        self.config = Conf()
        self.ui.lb_commom.setText(f'Todos os direitos reservados | Versão - {self.config.version} | {self.config.data}')
        
#################################################################
        
        ###instancia da tela de cadastro###
        self.telaCadastro = TelaCadastro()
        self.telaChamao =  TelaChamado()
        ####Pagina Inicial###

        self.ui.pages.setCurrentWidget(self.ui.page_ramal)


#################################################################

        ####Botões###
      
        self.ui.btn_db.clicked.connect(self.confDB)
        self.ui.btn_ramais.clicked.connect(self.ramal)
        self.ui.btn_add.clicked.connect(self.cadastrar)
        self.ui.btn_chamados.clicked.connect(self.chamado)
        self.ui.btn_chamados.clicked.connect(self.chamados)
        self.ui.btn_ramais.clicked.connect(self.list_ramal)
        self.ui.btn_search.clicked.connect(self.select_ramal)
        
#################################################################
   

    def chamado(self):

        self.telaChamao.show()
        self.hide()


    def cadastrar(self):
        self.telaCadastro.show()
        self.hide()

        ###conecxao banco de dados###
    def confDB(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "Select File", "", "All Files (*);;Text Files (*.txt)", options=options)
        connectionDB = open('connectDB.txt','w')
        connectionDB.write(file_name)
        connectionDB.close()

        ###paginas###
    def chamados(self):
        self.ui.pages.setCurrentWidget(self.ui.page_chamados)

    def ramal(self):
        self.ui.pages.setCurrentWidget(self.ui.page_ramal)    
    
    def color_row(self):
        ###Alterando a cor da celula de acordo com o valor###    
        item = self.ui.tb_ramal
         
        for row_color in range(item.rowCount()):
            text_status = item.item(row_color, 5)
            status = text_status.text()  
            if status == "Livre":
                item.item(row_color, 5).setBackground(QBrush(QColor(63, 235, 10)))
            elif status =="Atendendo":
                item.item(row_color, 5).setBackground(QBrush(QColor(170,170,127)))
            else:
                item.item(row_color, 5).setBackground(QBrush(QColor(255, 0, 0)))

    def select_line(self):
        
        item = self.ui.tb_ramal
        ##tabela###
        row = item.currentRow()
        nome = item.item(row,0).text()
        setor = item.item(row,1).text()
        status= item.item(row,5).text()
        if status == "Atendendo":
            status = "Livre"
        elif status == "Livre":
            status = "Atendendo"
        connect = Transact()
        connect.connect()
        connect.update_status(nome=nome, setor=setor, status=status)
        connect.fetchall()
        self.select_ramal()
        self.color_row()

    def list_ramal(self):
        
        ##tabela###
        item = self.ui.tb_ramal
        connect = Transact()
        connect.connect()   
        connect.list_ramal()
        result = connect.fetchall()
        item.setColumnCount(7)
        item.setRowCount((len(result)))
        for i in range(0,len(result)):
            for j in range(0,6):
                item.setItem(i,j,QTableWidgetItem(str(result[i][j])))
        for row_button in range(item.rowCount()):
            status = item.item(row_button,5).text()
            if status == "Atendendo":
                status = "Encerrar atendimento"
            elif status == "Livre":
                status = "Iniciar atendimento"    
            self.button = QPushButton(f"{status}")
            item.setCellWidget(row_button, 6, self.button)
            self.button.clicked.connect(self.select_line)
        self.color_row()    


    def select_ramal(self):
        item = self.ui.tb_ramal
        box = self.ui.cbb_select_setor
        setor = box.currentText()
        line = self.ui.le_search_name
        nome = line.text()

        ####conexaodb###
        connect = Transact()
        connect.connect()   
        connect.select_ramal(nome=nome,setor=setor)
        result = connect.fetchall()
        item.setColumnCount(7)
        item.setRowCount((len(result)))
        for i in range(0,len(result)):
            for j in range(0,6):
                item.setItem(i,j,QTableWidgetItem(str(result[i][j])))
        for row_button in range(item.rowCount()):
            status = item.item(row_button,5).text()
            if status == "Atendendo":
                status = "Encerrar atendimento"
            elif status == "Livre":
                status = "Iniciar atendimento"    
            self.button = QPushButton(f"{status}")
            item.setCellWidget(row_button, 6, self.button)
            self.button.clicked.connect(self.select_line)
        self.color_row()        
        
            
    
            
     


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec())
