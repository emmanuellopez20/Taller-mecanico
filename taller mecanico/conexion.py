import mysql.connector

class Conexion:
    def __init__(self):
        self.user = "root"
        self.password = ""
        self.database = "dbtaller_mecanico"
        self.host = "localhost"

    def open(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host, 
                user=self.user, 
                passwd=self.password, 
                database=self.database
            )
            if self.conn.is_connected():
                print("Conexión exitosa a la base de datos")
            return self.conn
        except mysql.connector.Error as err:
            print(f"Error al conectar con la base de datos: {err}")
            return None

    def close(self):
        if self.conn.is_connected():
            self.conn.close()
            print("Conexión cerrada")


