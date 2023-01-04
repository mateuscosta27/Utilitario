import json
import sqlite3

class Transact():
  
    with open("Connection.json") as stringConnection:
        connection = json.load(stringConnection)
    database= connection["connection"]
    conn = None
    cursor = None
    connected = False


    def connect(self):
        Transact.conn = sqlite3.connect(Transact.database)
        Transact.cursor = Transact.conn.cursor()
        Transact.connected = True

    def disconnect(self):
        Transact.conn.close()
        Transact.connect = False
    

    def execute(self,sql,params=None):
        if Transact.connected:
            if params == None:
                Transact.cursor.execute(sql)
            else:
                Transact.cursor.execute(sql,params)
                return True
        else:
             return False
    def fetchall(self):
        return Transact.cursor.fetchall()


    def persist(self):
        if Transact.connected:
            Transact.conn.commit()
            return True
        else:
            return False


    def select_ramal(self,nome,setor):
        self.nome = nome
        self.setor = setor
        self.execute(f"""
                SELECT  nome,
                        setor,
                        ramal_interno,
                        ramal_externo,
                        celular,
                        status
            FROM tb_funcionario t 
            WHERE t.setor LIKE '%{setor}%' 
            and t.nome LIKE '%{nome}%'
            """)   

    def list_ramal(self):
        self.execute(
            """
                SELECT  nome,
                        setor,
                        ramal_interno,
                        ramal_externo,
                        celular,
                        status
            FROM tb_funcionario"""
        )        

    def update_status(self,status,nome,setor):
        self.status = status
        self.nome = nome
        self.setor = setor
        self.box
        self.execute(
            f"""
                UPDATE tb_funcionario
                SET status = '{status}'
                WHERE nome = '{nome}'
                 AND setor = '{setor}'
        """
        )
        self.persist()

        



