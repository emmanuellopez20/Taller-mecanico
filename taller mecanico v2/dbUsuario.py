import mysql.connector
from mysql.connector import Error
import conexion as con
from usuario import Usuario

class dbUsuario:
    def save(self, usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            if self.conn is None:
                raise Exception("No se pudo conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO usuarios (nombre, username, password, perfil) VALUES (%s, %s, %s, %s)"
            self.datos = (usuario.getNombre(), usuario.getUsername(), usuario.getPassword(), usuario.getPerfil())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Datos insertados correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al guardar el usuario: {err}")
        except Exception as e:
            print(f"Error: {e}")

    def search(self, usuario_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM usuarios WHERE usuario_id = %s"
            self.cursor.execute(self.sql, (usuario_id,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                usuario = Usuario(row[0], row[1], row[2], row[3], row[4])
                return usuario
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el usuario: {err}")
            return None

    def edit(self, usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE usuarios SET nombre=%s, username=%s, password=%s, perfil=%s WHERE usuario_id=%s"
            self.datos = (usuario.getNombre(), usuario.getUsername(), usuario.getPassword(), usuario.getPerfil(), usuario.getUsuario_id())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al editar el usuario: {err}")

    def remov(self, usuario_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM usuarios WHERE usuario_id=%s"
            self.cursor.execute(self.sql, (usuario_id,))
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al eliminar el usuario: {err}")

    def getMaxId(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(usuario_id) FROM usuarios"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el máximo ID: {err}")
            return 0

    def autenticar(self, username, password):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
            self.cursor.execute(self.sql, (username, password))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                usuario = Usuario(row[0], row[1], row[2], row[3], row[4])
                return usuario
            return None
        except mysql.connector.Error as err:
            print(f"Error al autenticar el usuario: {err}")
            return None
