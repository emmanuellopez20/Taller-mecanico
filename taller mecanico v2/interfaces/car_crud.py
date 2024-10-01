import tkinter as tk
from tkinter import ttk, messagebox
from dbVehiculos import dbVehiculos
from vehiculo import Vehiculo
from dbClientes import dbClientes

class CarCRUD:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Vehículos")
        self.root.geometry("400x500")

        # Campos de entrada
        self.matricula_label = tk.Label(root, text="Matrícula")
        self.matricula_label.pack(anchor='w')
        self.txMatricula = tk.Entry(root)
        self.txMatricula.pack(anchor='w')

        self.cliente_label = tk.Label(root, text="Cliente")
        self.cliente_label.pack(anchor='w')
        self.cbClientes = ttk.Combobox(root)
        self.cbClientes.pack(anchor='w')
        self.cliente_id_label = tk.Label(root, text="ID del Cliente")
        self.cliente_id_label.pack(anchor='w')
        self.txClienteId = tk.Entry(root, state='readonly')
        self.txClienteId.pack(anchor='w')

        self.marca_label = tk.Label(root, text="Marca")
        self.marca_label.pack(anchor='w')
        self.txMarca = tk.Entry(root)
        self.txMarca.pack(anchor='w')

        self.modelo_label = tk.Label(root, text="Modelo")
        self.modelo_label.pack(anchor='w')
        self.txModelo = tk.Entry(root)
        self.txModelo.pack(anchor='w')

        # Botones
        self.btNuevo = tk.Button(root, text="Nuevo", command=self.nuevo_vehiculo)
        self.btNuevo.pack(side=tk.LEFT, padx=5, pady=5)

        self.btSalvar = tk.Button(root, text="Salvar", command=self.salvar_vehiculo)
        self.btSalvar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btSalvar.config(state=tk.DISABLED)

        self.btEditar = tk.Button(root, text="Editar", command=self.editar_vehiculo)
        self.btEditar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEditar.config(state=tk.DISABLED)

        self.btCancelar = tk.Button(root, text="Cancelar", command=self.cancelar)
        self.btCancelar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btCancelar.config(state=tk.DISABLED)

        self.btEliminar = tk.Button(root, text="Eliminar", command=self.eliminar_vehiculo)
        self.btEliminar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEliminar.config(state=tk.DISABLED)

        # Campo de búsqueda
        self.buscar_label = tk.Label(root, text="Buscar Matrícula")
        self.buscar_label.pack(anchor='center')
        self.txBuscarMatricula = tk.Entry(root)
        self.txBuscarMatricula.pack(anchor='center')
        self.btBuscar = tk.Button(root, text="Buscar", command=self.buscar_vehiculo)
        self.btBuscar.pack(anchor='center')

        self.cargar_clientes()

    def cargar_clientes(self):
        db_clientes = dbClientes()
        clientes = db_clientes.get_all()
        print(clientes)  # Verifica que los datos se están obteniendo
        self.clientes_dict = {cliente.getNombre(): cliente.getCliente_id() for cliente in clientes}
        self.cbClientes['values'] = list(self.clientes_dict.keys())
        self.cbClientes.bind("<<ComboboxSelected>>", self.mostrar_cliente_id)

    def mostrar_cliente_id(self, event):
        cliente_nombre = self.cbClientes.get()
        cliente_id = self.clientes_dict.get(cliente_nombre, "")
        self.txClienteId.config(state=tk.NORMAL)
        self.txClienteId.delete(0, tk.END)
        self.txClienteId.insert(0, cliente_id)
        self.txClienteId.config(state='readonly')

    def nuevo_vehiculo(self):
        self.txMatricula.delete(0, tk.END)
        self.txMarca.delete(0, tk.END)
        self.txModelo.delete(0, tk.END)
        self.cbClientes.set('')
        self.txClienteId.config(state=tk.NORMAL)
        self.txClienteId.delete(0, tk.END)
        self.txClienteId.config(state='readonly')

        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def salvar_vehiculo(self):
        matricula = self.txMatricula.get()
        marca = self.txMarca.get()
        modelo = self.txModelo.get()
        cliente_id = self.txClienteId.get()

        if not matricula or not marca or not modelo or not cliente_id:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        vehiculo = Vehiculo()
        vehiculo.setMatricula(matricula)
        vehiculo.setMarca(marca)
        vehiculo.setModelo(modelo)
        vehiculo.setCliente_id(cliente_id)

        db_vehiculos = dbVehiculos()
        db_vehiculos.save(vehiculo)

        messagebox.showinfo("Éxito", "Vehículo guardado exitosamente")
        self.nuevo_vehiculo()

    def cancelar(self):
        self.nuevo_vehiculo()

    def editar_vehiculo(self):
        matricula = self.txMatricula.get()
        marca = self.txMarca.get()
        modelo = self.txModelo.get()
        cliente_id = self.txClienteId.get()

        if not matricula or not marca or not modelo or not cliente_id:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        vehiculo = Vehiculo()
        vehiculo.setMatricula(matricula)
        vehiculo.setMarca(marca)
        vehiculo.setModelo(modelo)
        vehiculo.setCliente_id(cliente_id)

        db_vehiculos = dbVehiculos()
        db_vehiculos.edit(vehiculo)

        messagebox.showinfo("Éxito", "Vehículo editado exitosamente")
        self.nuevo_vehiculo()

    def eliminar_vehiculo(self):
        matricula = self.txMatricula.get()

        if not matricula:
            messagebox.showerror("Error", "Matrícula del vehículo es necesaria para eliminar")
            return

        db_vehiculos = dbVehiculos()
        db_vehiculos.remov(matricula)

        messagebox.showinfo("Éxito", "Vehículo eliminado exitosamente")
        self.nuevo_vehiculo()

    def buscar_vehiculo(self):
        matricula = self.txBuscarMatricula.get()

        if not matricula:
            messagebox.showerror("Error", "Matrícula del vehículo es necesaria para buscar")
            return

        db_vehiculos = dbVehiculos()
        vehiculo = db_vehiculos.search(matricula)

        if vehiculo:
            self.txMatricula.delete(0, tk.END)
            self.txMatricula.insert(0, vehiculo.getMatricula())
            self.txMarca.delete(0, tk.END)
            self.txMarca.insert(0, vehiculo.getMarca())
            self.txModelo.delete(0, tk.END)
            self.txModelo.insert(0, vehiculo.getModelo())
            self.txClienteId.config(state=tk.NORMAL)
            self.txClienteId.delete(0, tk.END)
            self.txClienteId.insert(0, vehiculo.getCliente_id())
            self.txClienteId.config(state='readonly')

            # Actualiza el combobox con el nombre del cliente
            cliente_id = vehiculo.getCliente_id()
            cliente_nombre = next((nombre for nombre, id in self.clientes_dict.items() if id == cliente_id), "")
            self.cbClientes.set(cliente_nombre)

            self.btSalvar.config(state=tk.DISABLED)
            self.btCancelar.config(state=tk.NORMAL)
            self.btEditar.config(state=tk.NORMAL)
            self.btEliminar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Vehículo no encontrado")
