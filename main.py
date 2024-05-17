# Autores Richard Boada 02230132006 - David Abril 02230132005

import tkinter as tk
from tkinter import ttk
import sqlite3
import os
from tkinter import messagebox

# Eliminar la base de datos existente si está presente
if os.path.exists('articulos.db'):
    os.remove('articulos.db')

# Crear una nueva conexión a la base de datos SQLite
conn = sqlite3.connect('articulos.db')
c = conn.cursor()

# Crear la tabla de artículos
c.execute('''CREATE TABLE IF NOT EXISTS articulos
             (id INTEGER PRIMARY KEY,
              nombre TEXT,
              precio REAL,
              especificaciones TEXT,
              color TEXT,
              descripcion TEXT,
              cantidad INTEGER,
              categoria TEXT)''')

# Crear la ventana principal
root = tk.Tk()
root.title("Tienda de Tecnología Cyberpunk")
root.geometry("600x400")

# Función para agregar un nuevo artículo a la base de datos
def agregar_articulo():
    nombre = nombre_entry.get()
    precio = precio_entry.get()
    especificaciones = especificaciones_entry.get()
    color = color_entry.get()
    descripcion = descripcion_entry.get("1.0", "end")
    cantidad = cantidad_entry.get()
    categoria = categoria_combo.get()

    c.execute('''INSERT INTO articulos (nombre, precio, especificaciones, color, descripcion, cantidad, categoria)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''', (nombre, precio, especificaciones, color, descripcion, cantidad, categoria))
    
    conn.commit()

    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", "El artículo se ha agregado correctamente.")

    # Limpiar los campos de entrada
    nombre_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)
    especificaciones_entry.delete(0, tk.END)
    color_entry.delete(0, tk.END)
    descripcion_entry.delete("1.0", tk.END)
    cantidad_entry.delete(0, tk.END)
    categoria_combo.set("")

# Función para mostrar la lista de artículos
def mostrar_lista():
    # Crear una nueva ventana
    lista_window = tk.Toplevel(root)
    lista_window.title("Lista de Artículos")
    
    # Crear un marco para organizar los widgets
    frame = ttk.Frame(lista_window)
    frame.pack(padx=10, pady=10, fill='both', expand=True)

    # Crear un árbol para mostrar la lista de artículos
    tree = ttk.Treeview(frame, columns=("Nombre", "Precio", "Especificaciones", "Color", "Descripción", "Cantidad", "Categoría"))
    tree.heading("#0", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Precio", text="Precio")
    tree.heading("Especificaciones", text="Especificaciones")
    tree.heading("Color", text="Color")
    tree.heading("Descripción", text="Descripción")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("Categoría", text="Categoría")

    # Obtener todos los artículos de la base de datos
    c.execute("SELECT * FROM articulos")
    filas = c.fetchall()

    # Insertar los datos en el árbol
    for fila in filas:
        tree.insert("", "end", text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]))

    tree.pack(expand=True, fill="both")

# Crear campos de entrada y etiquetas para agregar un nuevo artículo
nombre_label = ttk.Label(root, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

nombre_entry = ttk.Entry(root)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

precio_label = ttk.Label(root, text="Precio:")
precio_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

precio_entry = ttk.Entry(root)
precio_entry.grid(row=1, column=1, padx=5, pady=5)

especificaciones_label = ttk.Label(root, text="Especificaciones:")
especificaciones_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

especificaciones_entry = ttk.Entry(root)
especificaciones_entry.grid(row=2, column=1, padx=5, pady=5)

color_label = ttk.Label(root, text="Color:")
color_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

color_entry = ttk.Entry(root)
color_entry.grid(row=3, column=1, padx=5, pady=5)

descripcion_label = ttk.Label(root, text="Descripción:")
descripcion_label.grid(row=4, column=0, padx=5, pady=5, sticky="ne")

descripcion_entry = tk.Text(root, width=30, height=4)
descripcion_entry.grid(row=4, column=1, padx=5, pady=5)

cantidad_label = ttk.Label(root, text="Cantidad:")
cantidad_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")

cantidad_entry = ttk.Entry(root)
cantidad_entry.grid(row=5, column=1, padx=5, pady=5)

categoria_label = ttk.Label(root, text="Categoría:")
categoria_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")

categorias = ["Smartphones", "Laptops", "Accesorios", "Periféricos"] # Ejemplo de categorías de tecnología
categoria_combo = ttk.Combobox(root, values=categorias)
categoria_combo.grid(row=6, column=1, padx=5, pady=5)

# Botón para agregar un nuevo artículo
agregar_button = ttk.Button(root, text="Agregar Artículo", command=agregar_articulo)
agregar_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Botón para mostrar la lista de artículos
mostrar_lista_button = ttk.Button(root, text="Mostrar Lista de Artículos", command=mostrar_lista)
mostrar_lista_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

# Cerrar la conexión a la base de datos al salir
conn.close()

