#Brayan Armando Soria Ortiz
#programacion 3°B
#ventana para boleta de calificaciones
import tkinter as tk
ventana = tk.Tk()
ventana.title("Sistema de Venta de Aplicaciones")


etiqueta_cliente = tk.Label(ventana, text="Nombre del Cliente:")
etiqueta_cliente.pack()
entrada_cliente = tk.Entry(ventana)
entrada_cliente.pack()


boton_confirmar = tk.Button(ventana, text="Confirmar Venta", command=lambda: print("Venta realizada"))
boton_confirmar.pack()


ventana.mainloop()
