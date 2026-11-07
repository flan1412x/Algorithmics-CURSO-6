
import tkinter as tk
from tkinter import messagebox

# Función para permitir solo números y un punto decimal
def validar_numero(texto):
    if texto == "":
        return True

    if texto.count(".") > 1:
        return False

    return texto.replace(".", "", 1).isdigit()


# Función para calcular los ALGOTIHMICS
def calcular():
    try:
        sueldoP1 = float(entrada1.get())
        sueldoP2 = float(entrada2.get())
        sueldoP3 = float(entrada3.get())

        total = sueldoP1 + sueldoP2 + sueldoP3
        promedio = total / 3

        resultado.config(
            text=f"Total: ${total:.2f}\nPromedio: ${promedio:.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Debe ingresar los tres sueldos correctamente."
        )


# Función para limpiar los campos
def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    entrada3.delete(0, tk.END)
    resultado.config(text="Total: $0.00")


# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Sueldos")
ventana.geometry("360x350")
ventana.resizable(False, False)

# Configurar validación
validacion = ventana.register(validar_numero)

# Título
tk.Label(
    ventana, text="CALCULADORA DE SUELDOS",
    font=("Arial", 15, "bold")
).pack(pady=15)

# Entradas
tk.Label(ventana, text="Sueldo trabajador 1:").pack()
entrada1 = tk.Entry(
    ventana, validate="key",
    validatecommand=(validacion, "%P")
)
entrada1.pack()

tk.Label(ventana, text="Sueldo trabajador 2:").pack()
entrada2 = tk.Entry(
    ventana, validate="key",
    validatecommand=(validacion, "%P")
)
entrada2.pack()

tk.Label(ventana, text="Sueldo trabajador 3:").pack()
entrada3 = tk.Entry(
    ventana, validate="key",
    validatecommand=(validacion, "%P")
)
entrada3.pack()

# Botones
tk.Button(
    ventana, text="Calcular",
    command=calcular, bg="#4CAF50", fg="white",
    width=15
).pack(pady=10)

tk.Button(
    ventana, text="Limpiar",
    command=limpiar, width=15
).pack()

# Resultado
resultado = tk.Label(
    ventana, text="Total: $0.00",
    font=("Arial", 13, "bold")
)
resultado.pack(pady=15)

# Mantener la ventana abierta
ventana.mainloop()
