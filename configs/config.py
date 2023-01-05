import sqlite3
import sys, os
import json
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox
from datetime import date










class Conf():


    def __init__(self):
        data = date.today()
        dataAtual = data.strftime('%d/%m/%Y')
        self.data = dataAtual

        with open("version.json", encoding='utf8') as stringVersion:
            connection = json.load(stringVersion)
        principal= connection['VersionPrincipal']
        confConnection = connection['VersionConfConnection']
        chamado = connection['VersionChamado']



        self.principal = principal
        
    def select_local_db(self):

        selected_directory = QFileDialog.getExistingDirectory(dir="C:/")
        directory = (selected_directory+'/Utilitario/Banco')
        self.directory = directory

    def create_directory_db(self):

        dir_db = self.directory  
        if not os.path.exists(dir_db):
            os.makedirs(dir_db)
        sqlite3.connect(dir_db+'/utilitario.db')        
        self.create_json_db()
        


    def create_json_db(self):        
        dictonary_connection = {"connection":""}
        dictonary_connection["connection"] = self.directory+'/utilitario.db'
        insert = json.dumps(dictonary_connection, indent=4)
        with open("connection.json", "w") as outfile:
            outfile.write(insert)    
        
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


    