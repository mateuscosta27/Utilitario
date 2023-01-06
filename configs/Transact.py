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


    def create_tables(self):
        _sql_tb_setor = ("""
        CREATE TABLE IF NOT EXISTS tb_setor(
        "IdSetor"	INTEGER NOT NULL UNIQUE,
        "setor"	TEXT,
        PRIMARY KEY("IdSetor" AUTOINCREMENT));
        """)

        _sql_tb_status = (
            """
        CREATE TABLE IF NOT EXISTS tb_status(
        "IdStatus"	INTEGER NOT NULL UNIQUE,
        "status"	TEXT,
        PRIMARY KEY("IdStatus" AUTOINCREMENT));
        """
        )
        _sql_tb_funcionario =(
            """
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
        
        """
        ) 
        _sql_tb_municipio = (
            """
            CREATE TABLE IF NOT EXISTS tb_municipio(
                "IdMunicipio" INTEGER NOT NULL UNIQUE,
                "Nome" TEXT,
                primary key("IdMunicipio" AUTOINCREMENT)

            )
            """
        )
        _sql_tb_solicitante = (
            """
            CREATE TABLE IF NOT EXISTS tb_solicitante(
                "IdSolicitante" INTEGER NOT NULL UNIQUE,
                "Nome" TEXT,
                "Municipio" TEXT,

                PRIMARY KEY("IdSolicitante" AUTOINCREMENT)
                FOREIGN KEY("Municipio") REFERENCES "tb_municipio"("IdMunicipio")

            )
            """
            
        )
        tables = [_sql_tb_setor,_sql_tb_status,_sql_tb_funcionario,_sql_tb_municipio,_sql_tb_solicitante]
        for table in tables:
            self.connect()
            self.execute(table)
            self.persist()
            print(f'Tablela{table} criada com sucesso.')

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

        



