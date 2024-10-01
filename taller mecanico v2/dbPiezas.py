import mysql.connector
import conexion as con
from pieza import Pieza

class dbPiezas:
    def get_all(self):
        try:
            conn = con.conexion().open()
            cursor = conn.cursor()
            cursor.execute("SELECT pieza_id, descripcion, stock FROM piezas")
            rows = cursor.fetchall()
            conn.close()
            piezas = [Pieza(pieza_id=row[0], descripcion=row[1], stock=row[2]) for row in rows]
            return piezas
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def getMaxId(self):
        try:
            conn = con.conexion().open()
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(pieza_id) FROM piezas")
            max_id = cursor.fetchone()[0]
            conn.close()
            return max_id if max_id else 0
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 0

    def save(self, pieza):
        try:
            conn = con.conexion().open()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO piezas (descripcion, stock) VALUES (%s, %s)",
                           (pieza.getDescripcion(), pieza.getStock()))
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def edit(self, pieza):
        try:
            conn = con.conexion().open()
            cursor = conn.cursor()
            cursor.execute("UPDATE piezas SET descripcion=%s, stock=%s WHERE pieza_id=%s",
                        (pieza.getDescripcion(), pieza.getStock(), pieza.getPieza_id()))
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def remov(self, pieza_id):
        try:
            conn = con.conexion().open()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM piezas WHERE pieza_id=%s", (pieza_id,))
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def search(self, pieza_id):
        try:
            conn = con.conexion().open()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM piezas WHERE pieza_id=%s", (pieza_id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                return Pieza(pieza_id=row[0], descripcion=row[1], stock=row[2])
            return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
