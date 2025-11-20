import tkinter as tk

contador = 0

def contar():
    global contador
    contador += 1
    etiqueta.config(text=contador)

ventana = tk.Tk()
ventana.title("Clics")

etiqueta = tk.Label(ventana, text="0")
etiqueta.pack()

boton = tk.Button(ventana, text=" haga clic aquí", command=contar)
boton.pack()

ventana.mainloop()
