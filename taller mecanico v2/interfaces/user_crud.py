import tkinter as tk
from tkinter import ttk, messagebox
from dbUsuario import dbUsuario
from usuario import Usuario

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
        self.txPerfil.set('')

        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def salvar_usuario(self):
        nombre = self.txNombre.get()
        username = self.txUsername.get()
        password = self.txPassword.get()
        perfil = self.txPerfil.get()

        if not nombre or not username or not password or not perfil:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        usuario = Usuario()
        usuario.setNombre(nombre)
        usuario.setUsername(username)
        usuario.setPassword(password)
        usuario.setPerfil(perfil)

        db_usuario = dbUsuario()
        db_usuario.save(usuario)

        messagebox.showinfo("Éxito", "Usuario guardado exitosamente")
        self.nuevo_usuario()

    def cancelar(self):
        self.nuevo_usuario()

    def editar_usuario(self):
        usuario_id = self.txId.get()
        nombre = self.txNombre.get()
        username = self.txUsername.get()
        password = self.txPassword.get()
        perfil = self.txPerfil.get()

        if not usuario_id or not nombre or not username or not password or not perfil:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        usuario = Usuario()
        usuario.setUsuario_id(usuario_id)
        usuario.setNombre(nombre)
        usuario.setUsername(username)
        usuario.setPassword(password)
        usuario.setPerfil(perfil)

        db_usuario = dbUsuario()
        db_usuario.edit(usuario)

        messagebox.showinfo("Éxito", "Usuario editado exitosamente")
        self.nuevo_usuario()

    def eliminar_usuario(self):
        usuario_id = self.txId.get()

        if not usuario_id:
            messagebox.showerror("Error", "ID del usuario es necesario para eliminar")
            return

        db_usuario = dbUsuario()
        db_usuario.remov(usuario_id)

        messagebox.showinfo("Éxito", "Usuario eliminado exitosamente")
        self.nuevo_usuario()

    def buscar_usuario(self):
        usuario_id = self.txIngresarId.get()

        if not usuario_id:
            messagebox.showerror("Error", "ID del usuario es necesario para buscar")
            return

        db_usuario = dbUsuario()
        usuario = db_usuario.search(usuario_id)

        if usuario:
            self.txId.delete(0, tk.END)
            self.txId.insert(0, usuario.getUsuario_id())
            self.txNombre.delete(0, tk.END)
            self.txNombre.insert(0, usuario.getNombre())
            self.txUsername.delete(0, tk.END)
            self.txUsername.insert(0, usuario.getUsername())
            self.txPassword.delete(0, tk.END)
            self.txPassword.insert(0, usuario.getPassword())
            self.txPerfil.set(usuario.getPerfil())

            self.btEditar.config(state=tk.NORMAL)
            self.btCancelar.config(state=tk.NORMAL)
            self.btEliminar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Usuario no encontrado")
