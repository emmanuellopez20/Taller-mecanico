import tkinter as tk
from tkinter import messagebox
from dbPiezas import dbPiezas
from pieza import Pieza

class PiezaCRUD:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Piezas")
        self.root.geometry("400x300")

        # Campos de entrada
        self.id_label = tk.Label(root, text="ID")
        self.id_label.pack(anchor='w')
        self.txId = tk.Entry(root)
        self.txId.pack(anchor='w')

        self.descripcion_label = tk.Label(root, text="Descripción")
        self.descripcion_label.pack(anchor='w')
        self.txDescripcion = tk.Entry(root)
        self.txDescripcion.pack(anchor='w')

        self.stock_label = tk.Label(root, text="Stock")
        self.stock_label.pack(anchor='w')
        self.txStock = tk.Entry(root)
        self.txStock.pack(anchor='w')

        # Botones
        self.btNuevo = tk.Button(root, text="Nuevo", command=self.nueva_pieza)
        self.btNuevo.pack(side=tk.LEFT, padx=5, pady=5)

        self.btSalvar = tk.Button(root, text="Salvar", command=self.salvar_pieza)
        self.btSalvar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btSalvar.config(state=tk.DISABLED)

        self.btEditar = tk.Button(root, text="Editar", command=self.editar_pieza)
        self.btEditar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEditar.config(state=tk.DISABLED)

        self.btCancelar = tk.Button(root, text="Cancelar", command=self.cancelar)
        self.btCancelar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btCancelar.config(state=tk.DISABLED)

        self.btEliminar = tk.Button(root, text="Eliminar", command=self.eliminar_pieza)
        self.btEliminar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEliminar.config(state=tk.DISABLED)

        # Campo de búsqueda
        self.buscar_label = tk.Label(root, text="Buscar ID")
        self.buscar_label.pack(anchor='center')
        self.txBuscarId = tk.Entry(root)
        self.txBuscarId.pack(anchor='center')
        self.btBuscar = tk.Button(root, text="Buscar", command=self.buscar_pieza)
        self.btBuscar.pack(anchor='center')

    def nueva_pieza(self):
        self.txId.delete(0, tk.END)
        self.txDescripcion.delete(0, tk.END)
        self.txStock.delete(0, tk.END)

        db_piezas = dbPiezas()
        nuevo_id = db_piezas.getMaxId() + 1
        self.txId.insert(0, nuevo_id)

        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def salvar_pieza(self):
        descripcion = self.txDescripcion.get()
        stock = self.txStock.get()

        if not descripcion or not stock:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        pieza = Pieza()
        pieza.setDescripcion(descripcion)
        pieza.setStock(stock)

        db_piezas = dbPiezas()
        db_piezas.save(pieza)

        messagebox.showinfo("Éxito", "Pieza guardada exitosamente")
        self.nueva_pieza()

    def cancelar(self):
        self.nueva_pieza()

    def editar_pieza(self):
        pieza_id = self.txId.get()
        descripcion = self.txDescripcion.get()
        stock = self.txStock.get()

        if not pieza_id or not descripcion or not stock:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        pieza = Pieza()
        pieza.setPieza_id(pieza_id)
        pieza.setDescripcion(descripcion)
        pieza.setStock(stock)

        db_piezas = dbPiezas()
        db_piezas.edit(pieza)

        messagebox.showinfo("Éxito", "Pieza editada exitosamente")
        self.nueva_pieza()

    def eliminar_pieza(self):
        pieza_id = self.txId.get()

        if not pieza_id:
            messagebox.showerror("Error", "ID de la pieza es necesario para eliminar")
            return

        db_piezas = dbPiezas()
        db_piezas.remov(pieza_id)

        messagebox.showinfo("Éxito", "Pieza eliminada exitosamente")
        self.nueva_pieza()

    def buscar_pieza(self):
        pieza_id = self.txBuscarId.get()

        if not pieza_id:
            messagebox.showerror("Error", "ID de la pieza es necesario para buscar")
            return

        db_piezas = dbPiezas()
        pieza = db_piezas.search(pieza_id)

        if pieza:
            self.txId.delete(0, tk.END)
            self.txId.insert(0, pieza.getPieza_id())
            self.txDescripcion.delete(0, tk.END)
            self.txDescripcion.insert(0, pieza.getDescripcion())
            self.txStock.delete(0, tk.END)
            self.txStock.insert(0, pieza.getStock())

            self.btSalvar.config(state=tk.DISABLED)
            self.btCancelar.config(state=tk.NORMAL)
            self.btEditar.config(state=tk.NORMAL)
            self.btEliminar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Pieza no encontrada")