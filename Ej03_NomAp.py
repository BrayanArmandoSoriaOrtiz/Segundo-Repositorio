#Brayan Armando Soria Ortiz 
#Programacion
#Matutino 3°B
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de widgets en tkinter ")
ventana.geometry("400x500")

etiquet = tk.Label(ventana, text="Nombre:  ", font=("Arial", 13))7
etiquet.pack(pady=10)

entrad = tk.Entry(ventana, font=("Arial", 12))
entrad.pack(pady=5)

etiqueta = tk.Label(ventana, text="Apellido : ", font=("Arial", 13))
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)


def mostrar_texto():
    texto = entrad.get()
    texto2 = entrada.get()
    etiqueta_resultado.config(text=f"Tu nombre y apellido es : {texto} {texto2}")

boton = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="red")
etiqueta_resultado.pack(pady=5)

ventana.mainloop()

