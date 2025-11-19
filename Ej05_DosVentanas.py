#Brayan Armando Soria Ortiz
#programacion 3°B
#ventana para boleta de calificaciones
import tkinter as tk
from tkinter import ttk

def abrir_ventana1():
    ventana1 = tk.Toplevel(root)
    ventana1.title("Datos personales")
    ventana1.geometry("300x150")
    tk.Label(ventana1, text="nombre: Brayan ", font=("Arial", 12),fg="yellow").pack(pady=5)
    tk.Label(ventana1, text="Apellidos: Soria Ortiz", font=("Arial", 12),fg="red").pack(pady=5)

def abrir_ventana2():
        ventana2 = tk.Toplevel(root)
        ventana2.title("mensaje")
        ventana2.geometry("300x150")
        tk.Label(ventana2, text="programando con python ", font=("Arial", 12, "bold")).pack(expand=True)

root = tk.Tk()
root.title("ventana principal")
root.geometry("300x150")
        
boton1 = ttk.Button(root, text="mostrar nombre y apellidos ", command=abrir_ventana1)
boton1.pack(pady=20)

boton2 = ttk.Button(root, text="mosrtrar mensaje", command=abrir_ventana2)
boton2.pack(pady=10)

root.mainloop()