#Brayan Armando Soria Ortiz
#programacion 3°B
#ventana para boleta de calificaciones
import tkinter as tk

def Dolares():
    try:
       num=float(entrada1.get())
       res=num*0.054
       resultado.config(text=f"{num} pesos son {res:.2f} dolares")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

def Euros():
    try:
       num=float(entrada1.get())
       res=num*0.047
       resultado.config(text=f"{num} pesos son {res:.2f} euros")   
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

def Libras():
    try:
       num=float(entrada1.get())
       res=num*0.041
       resultado.config(text=f"{num} pesos son {res:.2f} Libras")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")
def Yenes():
    try:
       num=float(entrada1.get())
       res=num*8.20
       resultado.config(text=f"{num} pesos son {res:.2f} yenes")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tipo de Cambio")
ventana.geometry("350x230")

# Crear los cuadros de texto
entrada1 = tk.Entry(ventana)

entrada1.pack(pady=5)


# Crear botones para cada operación
boton_Dolares = tk.Button(ventana, text="Dolares", command=Dolares,bg="yellow", fg="Black")
boton_Dolares.pack(pady=5)

boton_Euros = tk.Button(ventana, text="Euros", command=Euros,bg="black", fg="white")
boton_Euros.pack(pady=5)

boton_Libras = tk.Button(ventana, text="Libras", command=Libras,bg="mediumaquamarine", fg="white")
boton_Libras.pack(pady=5)

boton_Yenes = tk.Button(ventana, text="Yenes", command=Yenes,bg="light pink", fg="white")
boton_Yenes.pack(pady=5)

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="El cambio es:", font=("Arial", 14))
resultado.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()