import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox
import conexion as con
from interfaces.menu import Menu
from interfaces.register import Register
from dbUsuario import dbUsuario


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")

        self.username_label = tk.Label(root, text="Usuario")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Contraseña")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

        self.register_button = tk.Button(root, text="Registrar", command=self.open_register)
        self.register_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            db_con = con.conexion()
            conn = db_con.open()
            if conn is None:
                raise Exception("No se pudo conectar a la base de datos")
            cursor = conn.cursor(buffered=True)
            cursor.execute("SELECT * FROM usuarios WHERE username=%s AND password=%s", (username, password))
            row = cursor.fetchone()
            db_con.close()

            if row:
                user_id = row[0]
                messagebox.showinfo("Éxito", "Login exitoso")
                self.open_menu(username, user_id)
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")

    def open_menu(self, username, user_id):
        self.root.withdraw()
        menu = tk.Toplevel(self.root)
        Menu(menu, username, user_id)

    def open_register(self):
        self.root.withdraw()
        register_window = tk.Toplevel(self.root)
        Register(register_window, self.root)
