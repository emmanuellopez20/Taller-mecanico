import tkinter as tk
from tkinter import messagebox
from dbUsuario import dbUsuario
from usuario import Usuario
from mysql.connector import Error

class Register:
    def __init__(self, root, login_window):
        self.root = root
        self.login_window = login_window
        self.root.title("Registro de Usuario")
        self.root.geometry("300x300")

        self.nombre_label = tk.Label(root, text="Nombre")
        self.nombre_label.pack(pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack(pady=5)

        self.username_label = tk.Label(root, text="Usuario")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Contraseña")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.perfil_label = tk.Label(root, text="Perfil")
        self.perfil_label.pack(pady=5)
        self.perfil_entry = tk.Entry(root)
        self.perfil_entry.pack(pady=5)

        self.register_button = tk.Button(root, text="Registrar", command=self.register)
        self.register_button.pack(pady=20)

    def register(self):
        nombre = self.nombre_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        perfil = self.perfil_entry.get()

        if nombre == "" or username == "" or password == "" or perfil == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            usuario = Usuario()
            usuario.setNombre(nombre)
            usuario.setUsername(username)
            usuario.setPassword(password)
            usuario.setPerfil(perfil)

            db_usuario = dbUsuario()
            db_usuario.save(usuario)

            messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
            self.root.destroy()
            self.login_window.deiconify()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")
