import mysql.connector
import conexion as con
from vehiculo import Vehiculo

class dbVehiculos:

    def get_all(self):
        try:
            conn = con.conexion().open()
            cursor = conn.cursor()
            cursor.execute("SELECT matricula, cliente_id FROM vehiculos")
            rows = cursor.fetchall()
            conn.close()
            vehiculos = [Vehiculo(matricula=row[0], cliente_id=row[1]) for row in rows]
            return vehiculos
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
    def save(self, vehiculo):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            if self.conn is None:
                raise Exception("No se pudo conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO vehiculos (matricula, marca, modelo, cliente_id) VALUES (%s, %s, %s, %s)"
            self.datos = (vehiculo.getMatricula(), vehiculo.getMarca(), vehiculo.getModelo(), vehiculo.getCliente_id())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Vehículo insertado correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al guardar el vehículo: {err}")
        except Exception as e:
            print(f"Error: {e}")

    def search(self, matricula):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM vehiculos WHERE matricula = %s"
            self.cursor.execute(self.sql, (matricula,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                vehiculo = Vehiculo(row[0], row[1], row[2], row[3])
                return vehiculo
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el vehículo: {err}")
            return None

    def edit(self, vehiculo):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE vehiculos SET marca = %s, modelo = %s, cliente_id = %s WHERE matricula = %s"
            self.datos = (vehiculo.getMarca(), vehiculo.getModelo(), vehiculo.getCliente_id(), vehiculo.getMatricula())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Vehículo actualizado correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al actualizar el vehículo: {err}")
        except Exception as e:
            print(f"Error: {e}")

    def remov(self, matricula):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM vehiculos WHERE matricula = %s"
            self.cursor.execute(self.sql, (matricula,))
            self.conn.commit()
            print("Vehículo eliminado correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al eliminar el vehículo: {err}")
        except Exception as e:
            print(f"Error: {e}")
