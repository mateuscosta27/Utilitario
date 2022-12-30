import sqlite3
import sys, os
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox
from sttle import *

class Conf():


    def __init__(self):


        app = QApplication(sys.argv)
        selected_directory = QFileDialog.getExistingDirectory(dir="C:/")
        self.directory = (selected_directory+'/Utilitario/Banco')
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            
    def create_database(self):
        conn = sqlite3.connect(self.directory+'/utilitario.db')
        cursor = conn.cursor()


        cursor.execute("""

        CREATE TABLE IF NOT EXISTS tb_setor(
        IdSetor INTEGER PRIMARY KEY AUTOINCREMENT,
        setor TEXT
        )    """)

        conn.commit()


        cursor.execute("""

        CREATE TABLE IF NOT EXISTS tb_funcionario(
        idFuncionario INTEGER PRIMARY KEY AUTOINCREMENT,
        funcionario TEXT,
        setor TEXT,
        ramal_interno TEXT,
        ramal_externo TEXT,
        celular TEXT,
        Id_setor INTEGER,
        CONSTRAINT fk_setor FOREIGN KEY (Id_setor) REFERENCES tb_setor)""")

        
        

teste = Conf()
teste.create_database()







    