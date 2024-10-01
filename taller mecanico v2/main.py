import tkinter as tk
from interfaces.login import Login

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()