import sqlite3
import sys, os
import json
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox
from datetime import date
from configs.Transact import *










class Conf():


    def __init__(self):
        data = date.today()
        dataAtual = data.strftime('%d/%m/%Y')
        self.data = dataAtual

        with open("version.json", encoding='utf8') as stringVersion:
            version = json.load(stringVersion)
        principal= version['VersionPrincipal']
        confConnection = version['VersionConfConnection']
        chamado = version['VersionChamado']

        self.principal = principal
        self.chamado = chamado
        self.confConnection = confConnection

    def version_update(self):
        with open("version.json", encoding="utf-8") as stringversion:
            version = json.load(stringversion)
            self.principal = '0.0.2-SNAPSHOT'
            self.chamado = '0.0.1-SNAPSHOT'
            self.confConnection = '0.0.1-SNAPSHOT'
                
        
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

    def create_tables(self):
        conn = Transact()
        conn.create_tables()
        conn.disconnect()


    