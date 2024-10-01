import mysql.connector
from conexion import conexion  # Asegúrate de que la ruta sea correcta
from reparacion import Reparacion

class dbReparaciones:
    def __init__(self):
        self.con = conexion()

    def getMaxId(self):
        try:
            conn = self.con.open()
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(reparacion_id) FROM reparaciones")
            max_id = cursor.fetchone()[0]
            conn.close()
            return max_id if max_id else 0
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 0
    def save(self, reparacion):
        try:
            conn = self.con.open()
            cursor = conn.cursor()
            sql = """
                INSERT INTO reparaciones (hora_entrada, fecha_entrada, matricula, cliente_id, tipo_servicio, pieza_id, cantidad_piezas, hora_salida, fecha_salida)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            datos = (
                reparacion.getHora_entrada(),
                reparacion.getFecha_entrada(),
                reparacion.getMatricula(),
                reparacion.getCliente_id(),
                reparacion.getTipo_servicio(),
                reparacion.getPieza_id(),
                reparacion.getCantidad_piezas(),
                reparacion.getHora_salida(),
                reparacion.getFecha_salida()
            )
            cursor.execute(sql, datos)
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error al guardar la reparación: {err}")


    def edit(self, reparacion):
        try:
            conn = self.con.open()
            cursor = conn.cursor()
            cursor.execute("UPDATE reparaciones SET hora_salida=%s, fecha_salida=%s, matricula=%s, cliente_id=%s, tipo_servicio=%s, pieza_id=%s, cantidad_piezas=%s WHERE reparacion_id=%s",
                        (reparacion.getHora_salida(), reparacion.getFecha_salida(), reparacion.getMatricula(), reparacion.getCliente_id(), reparacion.getTipo_servicio(), reparacion.getPieza_id(), reparacion.getCantidad_piezas(), reparacion.getReparacion_id()))
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def remov(self, reparacion_id):
        try:
            conn = self.con.open()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reparaciones WHERE reparacion_id=%s", (reparacion_id,))
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def search(self, reparacion_id):
        try:
            conn = self.con.open()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reparaciones WHERE reparacion_id=%s", (reparacion_id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                return Reparacion(reparacion_id=row[0], hora_entrada=row[1], hora_salida=row[2], fecha_entrada=row[3], fecha_salida=row[4], matricula=row[5], cliente_id=row[6], tipo_servicio=row[7], pieza_id=row[8], cantidad_piezas=row[9])
            return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
