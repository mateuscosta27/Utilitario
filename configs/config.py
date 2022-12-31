import sqlite3
import sys, os
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox

class Conf():


    def __init__(self):
        pass
    def craate_directory(self):
        app = QApplication(sys.argv)
        selected_directory = QFileDialog.getExistingDirectory(dir="C:/")
        self.directory = (selected_directory+'/Utilitario/Banco')
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def get_directory(self):
        get_dir = (self.directory+'/Utilitario/Banco')
        return get_dir
        
    def create_database(self):
        conn = sqlite3.connect(self.directory+'/utilitario.db')
        cursor = conn.cursor()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_setor(
        "IdSetor"	INTEGER NOT NULL UNIQUE,
        "setor"	TEXT,
        PRIMARY KEY("IdSetor" AUTOINCREMENT));
        """)
        conn.commit()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_status(
        "IdStatus"	INTEGER NOT NULL UNIQUE,
        "status"	TEXT,
        PRIMARY KEY("IdStatus" AUTOINCREMENT));
        """)
        conn.commit()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_funcionario(
        "IdFuncionario"	INTEGER NOT NULL UNIQUE,
        "Nome"	TEXT,
        "setor"	TEXT,
        "ramal_interno"	INTEGER,
        "ramal_externo"	INTEGER,
        "celular"	TEXT,
        "status"    TEXT,
        PRIMARY KEY("IdFuncionario" AUTOINCREMENT)
        FOREIGN KEY("setor") REFERENCES "tb_setor"("IdSetor")
        FOREIGN KEY("status") REFERENCES "tb_status"("IdStatus"));      
        
        """)
        conn.commit()

        


    def insert_itens(self):
        conn = sqlite3.connect(self.directory+'/utilitario.db')
        cursor = conn.cursor()
        ###Status###
        cursor.execute("""
        INSERT INTO tb_status (status) values ('Online'), ('Offline'), ('Ausente');
        """)

        conn.commit()

    get_database = property(dataget = get_directory)   








    