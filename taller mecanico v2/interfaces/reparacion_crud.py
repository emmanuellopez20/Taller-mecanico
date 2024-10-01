import tkinter as tk
from tkinter import ttk, messagebox
from dbReparaciones import dbReparaciones
from dbVehiculos import dbVehiculos
from dbPiezas import dbPiezas
from reparacion import Reparacion
from datetime import datetime

class ReparacionCRUD:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Reparaciones")
        self.root.geometry("600x400")

        # Campos de entrada
        self.id_label = tk.Label(root, text="ID")
        self.id_label.pack(anchor='w')
        self.txId = tk.Entry(root)
        self.txId.pack(anchor='w')

        self.hora_entrada_label = tk.Label(root, text="Hora de Entrada")
        self.hora_entrada_label.pack(anchor='w')
        self.txHoraEntrada = tk.Entry(root)
        self.txHoraEntrada.pack(anchor='w')

        self.hora_salida_label = tk.Label(root, text="Hora de Salida")
        self.hora_salida_label.pack(anchor='w')
        self.txHoraSalida = tk.Entry(root)
        self.txHoraSalida.pack(anchor='w')

        self.fecha_entrada_label = tk.Label(root, text="Fecha de Entrada")
        self.fecha_entrada_label.pack(anchor='w')
        self.txFechaEntrada = tk.Entry(root)
        self.txFechaEntrada.pack(anchor='w')

        self.fecha_salida_label = tk.Label(root, text="Fecha de Salida")
        self.fecha_salida_label.pack(anchor='w')
        self.txFechaSalida = tk.Entry(root)
        self.txFechaSalida.pack(anchor='w')

        self.matricula_label = tk.Label(root, text="Matrícula")
        self.matricula_label.pack(anchor='w')
        self.cbMatricula = ttk.Combobox(root)
        self.cbMatricula.pack(anchor='w')
        self.cbMatricula.bind("<<ComboboxSelected>>", self.mostrar_cliente_id)

        self.cliente_id_label = tk.Label(root, text="ID Cliente")
        self.cliente_id_label.pack(anchor='w')
        self.txClienteId = tk.Entry(root, state='readonly')
        self.txClienteId.pack(anchor='w')

        self.tipo_servicio_label = tk.Label(root, text="Tipo de Servicio")
        self.tipo_servicio_label.pack(anchor='w')
        self.txTipoServicio = tk.Entry(root)
        self.txTipoServicio.pack(anchor='w')

        self.pieza_label = tk.Label(root, text="Pieza")
        self.pieza_label.pack(anchor='w')
        self.cbPieza = ttk.Combobox(root)
        self.cbPieza.pack(anchor='w')
        self.cbPieza.bind("<<ComboboxSelected>>", self.mostrar_stock)

        self.stock_label = tk.Label(root, text="Stock")
        self.stock_label.pack(anchor='w')
        self.txStock = tk.Entry(root, state='readonly')
        self.txStock.pack(anchor='w')

        self.cantidad_piezas_label = tk.Label(root, text="Cantidad de Piezas")
        self.cantidad_piezas_label.pack(anchor='w')
        self.txCantidadPiezas = tk.Entry(root)
        self.txCantidadPiezas.pack(anchor='w')

        # Botones
        self.btNuevo = tk.Button(root, text="Nuevo", command=self.nueva_reparacion)
        self.btNuevo.pack(side=tk.LEFT, padx=5, pady=5)

        self.btSalvar = tk.Button(root, text="Salvar", command=self.salvar_reparacion)
        self.btSalvar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btSalvar.config(state=tk.DISABLED)

        self.btEditar = tk.Button(root, text="Editar", command=self.editar_reparacion)
        self.btEditar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEditar.config(state=tk.DISABLED)

        self.btCancelar = tk.Button(root, text="Cancelar", command=self.cancelar)
        self.btCancelar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btCancelar.config(state=tk.DISABLED)

        self.btEliminar = tk.Button(root, text="Eliminar", command=self.eliminar_reparacion)
        self.btEliminar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEliminar.config(state=tk.DISABLED)

        # Campo de búsqueda
        self.buscar_label = tk.Label(root, text="Buscar ID")
        self.buscar_label.pack(anchor='center')
        self.txBuscarId = tk.Entry(root)
        self.txBuscarId.pack(anchor='center')
        self.btBuscar = tk.Button(root, text="Buscar", command=self.buscar_reparacion)
        self.btBuscar.pack(anchor='center')

        self.cargar_matriculas()
        self.cargar_piezas()

    def cargar_matriculas(self):
        db_vehiculos = dbVehiculos()
        vehiculos = db_vehiculos.get_all()
        self.matriculas_dict = {vehiculo.getMatricula(): vehiculo.getCliente_id() for vehiculo in vehiculos}
        self.cbMatricula['values'] = list(self.matriculas_dict.keys())

    def cargar_piezas(self):
        db_piezas = dbPiezas()
        piezas = db_piezas.get_all()
        self.piezas_dict = {pieza.getDescripcion(): (pieza.getPieza_id(), pieza.getStock()) for pieza in piezas if pieza.getStock() > 0}
        self.cbPieza['values'] = list(self.piezas_dict.keys())

    def mostrar_cliente_id(self, event):
        matricula = self.cbMatricula.get()
        cliente_id = self.matriculas_dict.get(matricula, "")
        self.txClienteId.config(state=tk.NORMAL)
        self.txClienteId.delete(0, tk.END)
        self.txClienteId.insert(0, cliente_id)
        self.txClienteId.config(state='readonly')

    def mostrar_stock(self, event):
        pieza_descripcion = self.cbPieza.get()
        stock = self.piezas_dict.get(pieza_descripcion, ("", ""))[1]
        self.txStock.config(state=tk.NORMAL)
        self.txStock.delete(0, tk.END)
        self.txStock.insert(0, stock)
        self.txStock.config(state='readonly')

    def nueva_reparacion(self):
        self.txId.delete(0, tk.END)
        self.txHoraEntrada.delete(0, tk.END)
        self.txHoraSalida.delete(0, tk.END)
        self.txFechaEntrada.delete(0, tk.END)
        self.txFechaSalida.delete(0, tk.END)
        self.cbMatricula.set('')
        self.txClienteId.config(state=tk.NORMAL)
        self.txClienteId.delete(0, tk.END)
        self.txClienteId.config(state='readonly')
        self.txTipoServicio.delete(0, tk.END)
        self.cbPieza.set('')
        self.txStock.config(state=tk.NORMAL)
        self.txStock.delete(0, tk.END)
        self.txStock.config(state='readonly')
        self.txCantidadPiezas.delete(0, tk.END)

        db_reparaciones = dbReparaciones()
        nuevo_id = db_reparaciones.getMaxId() + 1
        self.txId.insert(0, nuevo_id)

        now = datetime.now()
        self.txHoraEntrada.insert(0, now.strftime("%H:%M:%S"))
        self.txFechaEntrada.insert(0, now.strftime("%Y-%m-%d"))

        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def salvar_reparacion(self):
        hora_entrada = self.txHoraEntrada.get()
        fecha_entrada = self.txFechaEntrada.get()
        matricula = self.cbMatricula.get()
        cliente_id = self.txClienteId.get()
        tipo_servicio = self.txTipoServicio.get()
        pieza_descripcion = self.cbPieza.get()
        cantidad_piezas = self.txCantidadPiezas.get()
        hora_salida = self.txHoraSalida.get()
        fecha_salida = self.txFechaSalida.get()

        if not hora_entrada or not fecha_entrada or not matricula or not cliente_id or not tipo_servicio or not cantidad_piezas:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if hora_salida and not self.validar_hora(hora_salida):
            messagebox.showerror("Error", "La hora de salida debe estar en formato HH:MM")
            return

        if fecha_salida and not self.validar_fecha(fecha_salida):
            messagebox.showerror("Error", "La fecha de salida debe estar en formato AAAA-MM-DD")
            return

        pieza_id, stock = self.piezas_dict.get(pieza_descripcion, (None, 0))
        if int(cantidad_piezas) > stock:
            messagebox.showerror("Error", "La cantidad de piezas no puede ser mayor al stock disponible")
            return

        reparacion = Reparacion()
        reparacion.setHora_entrada(hora_entrada)
        reparacion.setFecha_entrada(fecha_entrada)
        reparacion.setMatricula(matricula)
        reparacion.setCliente_id(cliente_id)
        reparacion.setTipo_servicio(tipo_servicio)
        reparacion.setPieza_id(pieza_id)
        reparacion.setCantidad_piezas(cantidad_piezas)
        if hora_salida:
            reparacion.setHora_salida(hora_salida)
        if fecha_salida:
            reparacion.setFecha_salida(fecha_salida)

        db_reparaciones = dbReparaciones()
        db_reparaciones.save(reparacion)

        messagebox.showinfo("Éxito", "Reparación guardada exitosamente")
        self.nueva_reparacion()


    def cancelar(self):
        self.nueva_reparacion()

    def editar_reparacion(self):
        reparacion_id = self.txId.get()
        hora_salida = self.txHoraSalida.get()
        fecha_salida = self.txFechaSalida.get()
        matricula = self.cbMatricula.get()
        cliente_id = self.txClienteId.get()
        tipo_servicio = self.txTipoServicio.get()
        pieza_descripcion = self.cbPieza.get()
        cantidad_piezas = self.txCantidadPiezas.get()

        if not hora_salida or not fecha_salida or not matricula or not cliente_id or not tipo_servicio or not cantidad_piezas:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        pieza_id, stock = self.piezas_dict.get(pieza_descripcion, (None, 0))
        if int(cantidad_piezas) > stock:
            messagebox.showerror("Error", "La cantidad de piezas no puede ser mayor al stock disponible")
            return

        reparacion = Reparacion()
        reparacion.setReparacion_id(reparacion_id)
        reparacion.setHora_salida(hora_salida)
        reparacion.setFecha_salida(fecha_salida)
        reparacion.setMatricula(matricula)
        reparacion.setCliente_id(cliente_id)
        reparacion.setTipo_servicio(tipo_servicio)
        reparacion.setPieza_id(pieza_id)
        reparacion.setCantidad_piezas(cantidad_piezas)

        db_reparaciones = dbReparaciones()
        db_reparaciones.edit(reparacion)

        messagebox.showinfo("Éxito", "Reparación editada exitosamente")
        self.nueva_reparacion()

    def eliminar_reparacion(self):
        reparacion_id = self.txId.get()

        if not reparacion_id:
            messagebox.showerror("Error", "ID de la reparación es necesario para eliminar")
            return

        db_reparaciones = dbReparaciones()
        db_reparaciones.remov(reparacion_id)

        messagebox.showinfo("Éxito", "Reparación eliminada exitosamente")
        self.nueva_reparacion()

    def buscar_reparacion(self):
        reparacion_id = self.txBuscarId.get()

        if not reparacion_id:
            messagebox.showerror("Error", "ID de la reparación es necesario para buscar")
            return

        db_reparaciones = dbReparaciones()
        reparacion = db_reparaciones.search(reparacion_id)

        if reparacion is None:
            messagebox.showerror("Error", "Reparación no encontrada")
            return

        self.txId.delete(0, tk.END)
        self.txId.insert(0, reparacion.getReparacion_id())
        self.txHoraEntrada.delete(0, tk.END)
        self.txHoraEntrada.insert(0, reparacion.getHora_entrada())
        self.txHoraSalida.delete(0, tk.END)
        if reparacion.getHora_salida() is not None:
            self.txHoraSalida.insert(0, reparacion.getHora_salida())
        self.txFechaEntrada.delete(0, tk.END)
        self.txFechaEntrada.insert(0, reparacion.getFecha_entrada())
        self.txFechaSalida.delete(0, tk.END)
        if reparacion.getFecha_salida() is not None:
            self.txFechaSalida.insert(0, reparacion.getFecha_salida())
        self.cbMatricula.set(reparacion.getMatricula())
        self.txClienteId.config(state=tk.NORMAL)
        self.txClienteId.delete(0, tk.END)
        self.txClienteId.insert(0, reparacion.getCliente_id())
        self.txClienteId.config(state='readonly')
        self.txTipoServicio.delete(0, tk.END)
        self.txTipoServicio.insert(0, reparacion.getTipo_servicio())
        pieza_id = reparacion.getPieza_id()
        pieza_descripcion = next((desc for desc, (id, _) in self.piezas_dict.items() if id == pieza_id), "")
        self.cbPieza.set(pieza_descripcion)
        self.txStock.config(state=tk.NORMAL)
        self.txStock.delete(0, tk.END)
        self.txStock.insert(0, self.piezas_dict.get(pieza_descripcion, ("", ""))[1])
        self.txStock.config(state='readonly')
        self.txCantidadPiezas.delete(0, tk.END)
        self.txCantidadPiezas.insert(0, reparacion.getCantidad_piezas())

        self.btSalvar.config(state=tk.DISABLED)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.NORMAL)
        self.btEliminar.config(state=tk.NORMAL)

    def validar_hora(self, hora):
        try:
            datetime.strptime(hora, "%H:%M")
            return True
        except ValueError:
            return False

    def validar_fecha(self, fecha):
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            return False


