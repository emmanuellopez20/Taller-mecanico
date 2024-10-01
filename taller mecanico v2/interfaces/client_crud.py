import tkinter as tk
from tkinter import messagebox
from dbClientes import dbClientes
from cliente import Cliente
from dbUsuario import dbUsuario

class ClientCRUD:
    def __init__(self, root, username, user_id):
        self.root = root
        self.user_id = user_id
        self.root.title("Gestión de Clientes")
        self.root.geometry("400x500")

        # Campos de entrada
        self.id_label = tk.Label(root, text="ID")
        self.id_label.pack(anchor='w')
        self.txId = tk.Entry(root)
        self.txId.pack(anchor='w')

        self.nombre_label = tk.Label(root, text="Nombre")
        self.nombre_label.pack(anchor='w')
        self.txNombreCliente = tk.Entry(root)
        self.txNombreCliente.pack(anchor='w')

        self.telefono_label = tk.Label(root, text="Teléfono")
        self.telefono_label.pack(anchor='w')
        self.txTelefono = tk.Entry(root)
        self.txTelefono.pack(anchor='w')

        # Campos de usuario
        self.usuario_id_label = tk.Label(root, text="ID del Usuario")
        self.usuario_id_label.pack(anchor='w')
        self.txUsuarioId = tk.Entry(root, state='readonly')
        self.txUsuarioId.pack(anchor='w')

        self.usuario_nombre_label = tk.Label(root, text="Nombre del Usuario")
        self.usuario_nombre_label.pack(anchor='w')
        self.txUsuarioNombre = tk.Entry(root, state='readonly')
        self.txUsuarioNombre.pack(anchor='w')

        # Botones
        self.btNuevo = tk.Button(root, text="Nuevo", command=self.nuevo_cliente)
        self.btNuevo.pack(side=tk.LEFT, padx=5, pady=5)

        self.btSalvar = tk.Button(root, text="Salvar", command=self.salvar_cliente)
        self.btSalvar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btSalvar.config(state=tk.DISABLED)

        self.btCancelar = tk.Button(root, text="Cancelar", command=self.cancelar)
        self.btCancelar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btCancelar.config(state=tk.DISABLED)

        self.btEditar = tk.Button(root, text="Editar", command=self.editar_cliente)
        self.btEditar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEditar.config(state=tk.DISABLED)

        self.btEliminar = tk.Button(root, text="Eliminar", command=self.eliminar_cliente)
        self.btEliminar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEliminar.config(state=tk.DISABLED)

        # Campo de búsqueda
        self.buscar_label = tk.Label(root, text="Buscar ID")
        self.buscar_label.pack(anchor='center')
        self.txIngresarId = tk.Entry(root)
        self.txIngresarId.pack(anchor='center')
        self.btBuscar = tk.Button(root, text="Buscar", command=self.buscar_cliente)
        self.btBuscar.pack(anchor='center')

    def nuevo_cliente(self):
        self.txId.delete(0, tk.END)
        self.txNombreCliente.delete(0, tk.END)
        self.txTelefono.delete(0, tk.END)
        self.txUsuarioId.config(state=tk.NORMAL)
        self.txUsuarioId.delete(0, tk.END)
        self.txUsuarioId.config(state='readonly')
        self.txUsuarioNombre.config(state=tk.NORMAL)
        self.txUsuarioNombre.delete(0, tk.END)
        self.txUsuarioNombre.config(state='readonly')

        db_clientes = dbClientes()
        nuevo_id = db_clientes.getMaxId() + 1
        self.txId.insert(0, nuevo_id)

        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def salvar_cliente(self):
        nombre = self.txNombreCliente.get()
        telefono = self.txTelefono.get()

        if not nombre or not telefono:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        cliente = Cliente()
        cliente.setNombre(nombre)
        cliente.setTelefono(telefono)

        db_clientes = dbClientes()
        db_clientes.save(cliente, self.user_id)

        messagebox.showinfo("Éxito", "Cliente guardado exitosamente")
        self.nuevo_cliente()

    def cancelar(self):
        self.nuevo_cliente()

    def editar_cliente(self):
        cliente_id = self.txId.get()
        nombre = self.txNombreCliente.get()
        telefono = self.txTelefono.get()

        if not cliente_id or not nombre or not telefono:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        cliente = Cliente()
        cliente.setCliente_id(cliente_id)
        cliente.setNombre(nombre)
        cliente.setTelefono(telefono)

        db_clientes = dbClientes()
        db_clientes.edit(cliente)

        messagebox.showinfo("Éxito", "Cliente editado exitosamente")
        self.nuevo_cliente()

    def eliminar_cliente(self):
        cliente_id = self.txId.get()

        if not cliente_id:
            messagebox.showerror("Error", "ID del cliente es necesario para eliminar")
            return

        db_clientes = dbClientes()
        db_clientes.remov(cliente_id)

        messagebox.showinfo("Éxito", "Cliente eliminado exitosamente")
        self.nuevo_cliente()

    def buscar_cliente(self):
        cliente_id = self.txIngresarId.get()

        if not cliente_id:
            messagebox.showerror("Error", "ID del cliente es necesario para buscar")
            return

        db_clientes = dbClientes()
        cliente = db_clientes.search(cliente_id)

        if cliente:
            self.txId.delete(0, tk.END)
            self.txId.insert(0, cliente.getCliente_id())
            self.txNombreCliente.delete(0, tk.END)
            self.txNombreCliente.insert(0, cliente.getNombre())
            self.txTelefono.delete(0, tk.END)
            self.txTelefono.insert(0, cliente.getTelefono())

            # Obtener información del usuario que registró el cliente
            db_usuario = dbUsuario()
            usuario = db_usuario.search(cliente.getUsuario_id())

            if usuario:
                self.txUsuarioId.config(state=tk.NORMAL)
                self.txUsuarioId.delete(0, tk.END)
                self.txUsuarioId.insert(0, usuario.getUsuario_id())
                self.txUsuarioId.config(state='readonly')
                self.txUsuarioNombre.config(state=tk.NORMAL)
                self.txUsuarioNombre.delete(0, tk.END)
                self.txUsuarioNombre.insert(0, usuario.getNombre())
                self.txUsuarioNombre.config(state='readonly')

            self.btEditar.config(state=tk.NORMAL)
            self.btCancelar.config(state=tk.NORMAL)
            self.btEliminar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Cliente no encontrado")
