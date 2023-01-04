import sqlite3
import sys, os
import json
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox

class Conf():


    def __init__(self):
        pass
    def craate_directory(self):
        app = QApplication(sys.argv)
        selected_directory = QFileDialog.getExistingDirectory(dir="C:/")
        directory = (selected_directory+'/Utilitario/Banco')
        if not os.path.exists(directory):
            os.makedirs(directory)
        dictonary_connection = {"connection":""}
        dictonary_connection["connection"] = directory
        inserir = json.dumps(dictonary_connection, indent=4)
        with open("connection.json", "w") as outfile:
            outfile.write(inserir)    

        
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
        "ramal_interno"	TEXT,
        "ramal_externo"	TEXT,
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



conf = Conf()
conf.craate_directory()





    