import tkinter as tk
from tkinter import messagebox
import mysql.connector
import conexion as con
import usuario as user

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

    def search(self, usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            aux = None
            self.sql = "SELECT * FROM usuarios WHERE usuario_id = {}".format(usuario.getUsuario_id())
            self.cursor1.execute(self.sql)
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.con.close()
            if row[0] is not None:
                aux = user.usuario()
                aux.setUsuario_id(int(row[0]))
                aux.setNombre(row[1])
                aux.setUsername(row[2])
                aux.setPassword(row[3])
                aux.setPerfil(row[4])
        except:
            print("")
        return aux

    def edit(self, usuario):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "UPDATE usuarios SET nombre=%s, username=%s, password=%s, perfil=%s WHERE usuario_id=%s"
        self.datos = (usuario.getNombre(), usuario.getUsername(), usuario.getPassword(), usuario.getPerfil(), usuario.getUsuario_id())
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.con.close()

    def remov(self, usuario):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "DELETE FROM usuarios WHERE usuario_id={}".format(usuario.getUsuario_id())
        self.cursor1.execute(self.sql)
        self.conn.commit()
        self.con.close()

    def getMaxId(self):
        self.con = con.Conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "SELECT MAX(usuario_id) FROM usuarios"
        self.cursor1.execute(self.sql)
        row = self.cursor1.fetchone()
        self.conn.commit()
        self.con.close()
        return row[0] if row[0] is not None else 1


    def Auntenticar(self, usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            aux = None
            self.sql = "SELECT * FROM usuarios WHERE username = '{}'".format(usuario.getUsername())
            self.cursor1.execute(self.sql)
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.con.close()
            if row[0] is not None:
                if usuario.getPassword() == row[3]:
                    aux = user.usuario()
                    aux.setUsuario_id(int(row[0]))
                    aux.setNombre(row[1])
                    aux.setUsername(row[2])
                    aux.setPassword(row[3])
                    aux.setPerfil(row[4])
        except:
            print("")
        return aux

    def close(self):
        if self.conn.is_connected():
            self.conn.close()
