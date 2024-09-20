import tkinter as tk
from tkinter import messagebox, ttk
import conexion as con
import usuario as user
import dbUsuario as db
import mysql.connector

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
            db_con = con.Conexion()
            conn = db_con.open()
            if conn is None:
                raise Exception("No se pudo conectar a la base de datos")
            cursor = conn.cursor(buffered=True)
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
        archivo_menu.add_command(label="Usuarios", command=self.open_user_crud)
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

    def open_user_crud(self):
        user_window = tk.Toplevel(self.root)
        UserCRUD(user_window)

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

class UserCRUD:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Usuarios")
        self.root.geometry("400x400")

        # Campos de entrada
        self.id_label = tk.Label(root, text="ID")
        self.id_label.pack(anchor='w')
        self.txId = tk.Entry(root)
        self.txId.pack(anchor='w')

        self.nombre_label = tk.Label(root, text="Nombre")
        self.nombre_label.pack(anchor='w')
        self.txNombre = tk.Entry(root)
        self.txNombre.pack(anchor='w')

        self.username_label = tk.Label(root, text="Usuario")
        self.username_label.pack(anchor='w')
        self.txUsername = tk.Entry(root)
        self.txUsername.pack(anchor='w')

        self.password_label = tk.Label(root, text="Contraseña")
        self.password_label.pack(anchor='w')
        self.txPassword = tk.Entry(root, show="*")
        self.txPassword.pack(anchor='w')

        self.perfil_label = tk.Label(root, text="Perfil")
        self.perfil_label.pack(anchor='w')
        self.txPerfil = ttk.Combobox(root, values=["privado", "publico"])
        self.txPerfil.pack(anchor='w')

        # Botones
        self.btNuevo = tk.Button(root, text="Nuevo", command=self.nuevo_usuario)
        self.btNuevo.pack(side=tk.LEFT, padx=5, pady=5)

        self.btSalvar = tk.Button(root, text="Salvar", command=self.salvar_usuario)
        self.btSalvar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btSalvar.config(state=tk.DISABLED)

        self.btCancelar = tk.Button(root, text="Cancelar", command=self.cancelar)
        self.btCancelar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btCancelar.config(state=tk.DISABLED)

        self.btEditar = tk.Button(root, text="Editar", command=self.editar_usuario)
        self.btEditar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEditar.config(state=tk.DISABLED)

        self.btEliminar = tk.Button(root, text="Eliminar", command=self.eliminar_usuario)
        self.btEliminar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEliminar.config(state=tk.DISABLED)

        # Campo de búsqueda
        self.buscar_label = tk.Label(root, text="Buscar ID")
        self.buscar_label.pack(anchor='center')
        self.txIngresarId = tk.Entry(root)
        self.txIngresarId.pack(anchor='center')
        self.btBuscar = tk.Button(root, text="Buscar", command=self.buscar_usuario)
        self.btBuscar.pack(anchor='center')

    def nuevo_usuario(self):
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txUsername.delete(0, tk.END)
        self.txPassword.delete(0, tk.END)
        self.txPerfil.set("")

        try:
            db_con = con.Conexion()
            conn = db_con.open()
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(usuario_id) FROM usuarios")
            max_id = cursor.fetchone()[0]
            nuevo_id = (max_id + 1) if max_id else 1
            self.txId.insert(0, nuevo_id)
            db_con.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")

        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def buscar_usuario(self):
        id_usuario = self.txIngresarId.get()
        try:
            db_con = con.Conexion()
            conn = db_con.open()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario_id=%s", (id_usuario,))
            usuario = cursor.fetchone()
            db_con.close()

            if usuario:
                self.txId.delete(0, tk.END)
                self.txId.insert(0, usuario[0])
                self.txNombre.delete(0, tk.END)
                self.txNombre.insert(0, usuario[1])
                self.txUsername.delete(0, tk.END)
                self.txUsername.insert(0, usuario[2])
                self.txPassword.delete(0, tk.END)
                self.txPassword.insert(0, usuario[3])
                self.txPerfil.set(usuario[4])

                self.btEditar.config(state=tk.NORMAL)
                self.btCancelar.config(state=tk.NORMAL)
                self.btEliminar.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Error", "Usuario no encontrado")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")


            if usuario:
                self.txId.delete(0, tk.END)
                self.txId.insert(0, usuario[0])
                self.txNombre.delete(0, tk.END)
                self.txNombre.insert(0, usuario[1])
                self.txUsername.delete(0, tk.END)
                self.txUsername.insert(0, usuario[2])
                self.txPassword.delete(0, tk.END)
                self.txPassword.insert(0, usuario[3])
                self.txPerfil.set(usuario[4])

                self.btEditar.config(state=tk.NORMAL)
                self.btCancelar.config(state=tk.NORMAL)
                self.btEliminar.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Error", "Usuario no encontrado")
        except mysql.connector.Error as err:messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")


    def validar_entrada(self):
        if not self.txId.get().isdigit():
            messagebox.showerror("Error", "El ID debe ser un número entero")
            return False
        if not self.txUsername.get():
            messagebox.showerror("Error", "El nombre de usuario no puede estar vacío")
            return False
        return True

    def salvar_usuario(self):
        if not self.validar_entrada():
            return
        try:
            db_con = con.Conexion()
            conn = db_con.open()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (usuario_id, nombre, username, password, perfil) VALUES (%s, %s, %s, %s, %s)",
                (self.txId.get(), self.txNombre.get(), self.txUsername.get(), self.txPassword.get(), self.txPerfil.get())
                )
            conn.commit()
            db_con.close()
            messagebox.showinfo("Información", "Usuario guardado exitosamente")

            # Limpiar campos de entrada
            self.txId.delete(0, tk.END)
            self.txNombre.delete(0, tk.END)
            self.txUsername.delete(0, tk.END)
            self.txPassword.delete(0, tk.END)
            self.txPerfil.set("")

            # Deshabilitar botones
            self.btSalvar.config(state=tk.DISABLED)
            self.btCancelar.config(state=tk.DISABLED)
            self.btEditar.config(state=tk.DISABLED)
            self.btEliminar.config(state=tk.DISABLED)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")

    def editar_usuario(self):
        if not self.validar_entrada():
            return
        try:
            db_con = con.Conexion()
            conn = db_con.open()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE usuarios SET nombre=%s, username=%s, password=%s, perfil=%s WHERE usuario_id=%s",
                (self.txNombre.get(), self.txUsername.get(), self.txPassword.get(), self.txPerfil.get(), self.txId.get())
                )
            conn.commit()
            db_con.close()
            messagebox.showinfo("Información", "Usuario editado exitosamente")

            # Limpiar campos de entrada
            self.txId.delete(0, tk.END)
            self.txNombre.delete(0, tk.END)
            self.txUsername.delete(0, tk.END)
            self.txPassword.delete(0, tk.END)
            self.txPerfil.set("")

            # Deshabilitar botones
            self.btEditar.config(state=tk.DISABLED)
            self.btCancelar.config(state=tk.DISABLED)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")
    def eliminar_usuario(self):
        id_usuario = self.txId.get()
        try:
            db_con = con.Conexion()
            conn = db_con.open()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE usuario_id=%s", (id_usuario,))
            conn.commit()
            db_con.close()
            messagebox.showinfo("Información", "Usuario eliminado exitosamente")

            # Limpiar campos de entrada
            self.txId.delete(0, tk.END)
            self.txNombre.delete(0, tk.END)
            self.txUsername.delete(0, tk.END)
            self.txPassword.delete(0, tk.END)
            self.txPerfil.set("")

        # Deshabilitar botones
            self.btEliminar.config(state=tk.DISABLED)
            self.btCancelar.config(state=tk.DISABLED)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")
    def cancelar(self):
        # Limpiar campos de entrada
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txUsername.delete(0, tk.END)
        self.txPassword.delete(0, tk.END)
        self.txPerfil.set("")

        # Deshabilitar botones
        self.btSalvar.config(state=tk.DISABLED)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()


