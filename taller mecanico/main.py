import tkinter as tk
from tkinter import messagebox
import mysql.connector
import conexion as con
import dbUsuario as db
import usuario as user

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.root.geometry("300x200")

        self.username_label = tk.Label(root, text="Usuario")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Contraseña")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(root, text="Acceder", command=self.login)
        self.login_button.pack(pady=5)

        self.register_button = tk.Button(root, text="Registrar Nuevo Usuario", command=self.open_register)
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
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE username=%s AND password=%s", (username, password))
            row = cursor.fetchone()
            db_con.close()

            if row:
                messagebox.showinfo("Éxito", "Login exitoso")
                self.open_menu()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")

    def open_menu(self):
        self.root.withdraw()
        menu = tk.Toplevel(self.root)
        menu.title("Menú Principal")
        menu.geometry("400x300")

        menubar = tk.Menu(menu)
        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Usuarios")
        archivo_menu.add_command(label="Clientes")
        archivo_menu.add_command(label="Carros")
        archivo_menu.add_command(label="Piezas")
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        menu.config(menu=menubar)

    def open_register(self):
        self.root.withdraw()
        register_window = tk.Toplevel(self.root)
        Register(register_window, self.root)

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
            usuario = user.Usuario()
            usuario.setNombre(nombre)
            usuario.setUsername(username)
            usuario.setPassword(password)
            usuario.setPerfil(perfil)

            db_usuario = db.dbUsuario()
            db_usuario.save(usuario)

            messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
            self.root.destroy()
            self.login_window.deiconify()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()


