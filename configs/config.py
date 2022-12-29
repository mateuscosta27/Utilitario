import sqlite3
import sys, os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from sttle import *

class Conf():


    def __init__(self):
        app = QApplication(sys.argv)
        selected_directory = QFileDialog.getExistingDirectory(directory="C:/")
        self.directory = (selected_directory+'/Utilitario/Banco')
        if not os.path.exists(self.directory):
            information = QMessageBox()
            information.setIcon(QMessageBox.Information)
            information.setText(f"Os arquivos serão salvos no destino {self.directory}")
            information.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            response = information.exec_()
            if response == QMessageBox.Ok:
                os.makedirs(self.directory)  
                create = QMessageBox()
                create.setText("Os diretórios foram criados com sucesso!")
                create.exec_()
                
    def create_database(self):
        db = sqlite3.connect(self.directory+'/utilitario.db')
        cursor = db.cursor()
        cursor.execute(
            """"
            CREATE TABLE IF NOT EXISTS tb_setor (
                IdSetor INT PRIMARY KEY,
                nome text)
                """)
        db.commit()

        cursor.execute(
            """""
            CREATE TABLE IF NOT EXISTS tb_funcionario (
                IdFuncionario  PRIMARY KEY AUTOINCREMENT,
                Funcionario text,
                Setor text,
                ramal_interno text,
                ramal_externo text,
                celular text,
                Id_setor INT foreign key REFERENCES tb_setor(IdSetor)
            """
        )
        db.commit()
            

teste = Conf()
teste.create_database()







    