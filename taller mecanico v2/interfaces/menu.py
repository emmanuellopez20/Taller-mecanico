import tkinter as tk
from interfaces.user_crud import UserCRUD
from interfaces.client_crud import ClientCRUD
from interfaces.car_crud import CarCRUD
from interfaces.pieza_crud import PiezaCRUD
from interfaces.reparacion_crud import ReparacionCRUD

class Menu:
    def __init__(self, root, username, user_id):
        self.root = root
        self.root.title("Menú Principal")
        self.root.geometry("400x300")

        menubar = tk.Menu(root)
        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Usuarios", command=self.open_user_crud)
        archivo_menu.add_command(label="Clientes", command=lambda: self.open_client_crud(username, user_id))
        archivo_menu.add_command(label="Carros", command=self.open_car_crud)
        archivo_menu.add_command(label="Piezas", command=self.open_pieza_crud)
        archivo_menu.add_command(label="Reparaciones", command=self.open_reparacion_crud)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        root.config(menu=menubar)

    def open_user_crud(self):
        user_window = tk.Toplevel(self.root)
        UserCRUD(user_window)

    def open_client_crud(self, username, user_id):
        client_window = tk.Toplevel(self.root)
        ClientCRUD(client_window, username, user_id)
    
    def open_car_crud(self):
        new_window = tk.Toplevel(self.root)
        CarCRUD(new_window)  # Abre la interfaz de gestión de vehículos

    def open_reparacion_crud(self):
        new_window = tk.Toplevel(self.root)
        ReparacionCRUD(new_window)
    
    def open_pieza_crud(self):
        new_window = tk.Toplevel(self.root)
        PiezaCRUD(new_window)