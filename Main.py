import sys
from View.Principal import *
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sqlite3


class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.list_ramal()

        ####Pagina Inicial###

        self.ui.pages.setCurrentWidget(self.ui.page_ramal)


        ####Botões###
        self.ui.btn_chamados.clicked.connect(self.chamados)
        self.ui.btn_ramais.clicked.connect(self.ramal)
        self.ui.btn_ramais.clicked.connect(self.list_ramal)
        self.ui.btn_db.clicked.connect(self.confDB)

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

    def list_ramal(self):
        init = open('connectDB.txt','r')
        directoryDB = init.read()
        item = self.ui.tb_ramal
        conn = sqlite3.connect(directoryDB)
        cursor = conn.cursor()
        cursor.execute("""
                SELECT  nome,
                        ramal_interno,
                        ramal_externo,
                        celular,
                        status
            FROM tb_funcionario""")
        result = cursor.fetchall()
        item.setColumnCount(6)
        item.setRowCount((len(result)))
        
        for i in range(0,len(result)):
            for j in range(0,5):
                item.setItem(i,j,QTableWidgetItem(str(result[i][j])))
                button = QPushButton("Abrir chamado")
                style = (u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 15px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 5px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
                button.setStyleSheet(style)
                item.setCellWidget(i,5,button)
        conn.close()        
   
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec())
