import re
from tkinter import messagebox

def validate_email(email):
    """
    Valida si el email tiene un formato correcto.
    """
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    else:
        return False

def show_error(message):
    """
    Muestra un mensaje de error en una ventana emergente.
    """
    messagebox.showerror("Error", message)

def show_info(message):
    """
    Muestra un mensaje de información en una ventana emergente.
    """
    messagebox.showinfo("Información", message)

def validate_not_empty(fields):
    """
    Valida que los campos no estén vacíos.
    """
    for field in fields:
        if not field.get():
            return False
    return True
