import tkinter as tk
from tkinter import messagebox


ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("300x400")


def agregar_tarea():
    tarea = entrada.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning(" Por favor, escribe una tarea.")


def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)
    else:
        messagebox.showwarning(" Selecciona una tarea para eliminar.")


entrada = tk.Entry(ventana, width=25)
entrada.pack(pady=10)


btn_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)
btn_agregar.pack()


lista_tareas = tk.Listbox(ventana, width=30, height=15)
lista_tareas.pack(pady=10)


btn_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea)
btn_eliminar.pack()

ventana.mainloop()
