import tkinter as tk #Respuesta 7, acá vemos el tkinter
from tkinter import Menu
from tkinter import messagebox

# Clase Receta para almacenar nombre y lista de ingredientes
class Receta: #Respuesta 2 acerca de "class"
    def __init__(self, nombre, ingredientes): #Respuesta 3, acá se inicializan los atributos del objeto
        self.nombre = nombre
        self.ingredientes = ingredientes

# Clase GestorRecetas para gestionar las recetas
class GestorRecetas: #Respuesta 2 acerca de "class"
    def __init__(self): #Respuesta 3, acá se inicializan los atributos del objeto
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)

    def eliminar_receta(self, indice):
        try:
            receta_eliminada = self.recetas.pop(indice)
            return receta_eliminada.nombre
        except IndexError:
            return None

# Función para agregar una nueva receta
def agregar_receta():  #Respuesta 6, acá podemos ver la indentación en Python
    nombre = entry_nombre.get()
    ingredientes = entry_ingredientes.get().split(",")
    
    if nombre and ingredientes:
        gestor.agregar_receta(nombre, ingredientes)
        listbox_recetas.insert(tk.END, nombre)
        entry_nombre.delete(0, tk.END)
        entry_ingredientes.delete(0, tk.END)
        messagebox.showinfo("Receta agregada", f"La receta '{nombre}' ha sido agregada.")
    else:
        messagebox.showwarning("Error", "Por favor, ingrese un nombre y al menos un ingrediente.")

# Función para mostrar los ingredientes de una receta seleccionada
def ver_ingredientes():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        receta = gestor.recetas[indice]
        ingredientes = ", ".join(receta.ingredientes)
        messagebox.showinfo(f"Ingredientes de {receta.nombre}", f"{ingredientes}")
    else:
        messagebox.showwarning("Error", "Seleccione una receta para ver sus ingredientes.")

# Función para eliminar una receta seleccionada
def eliminar_receta():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        nombre = gestor.eliminar_receta(indice)
        if nombre:
            listbox_recetas.delete(indice)
            messagebox.showinfo("Receta eliminada", f"La receta '{nombre}' ha sido eliminada.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar la receta.")
    else:
        messagebox.showwarning("Error", "Seleccione una receta para eliminar.")

# Crear la ventana principal
ventana = tk.Tk() #Respuesta 7, acá vemos tk tkinter
ventana.title("Gestor de Recetas")

# Instancia del gestor de recetas
gestor = GestorRecetas()

# Etiquetas y entradas para el nombre y los ingredientes
label_nombre = tk.Label(ventana, text="Nombre de la receta:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_ingredientes = tk.Label(ventana, text="Ingredientes (separados por coma):")
label_ingredientes.pack()
entry_ingredientes = tk.Entry(ventana)
entry_ingredientes.pack()

#Para crear el menú
def crear_menu(ventana): 
        barra_menu = Menu(ventana)
        ventana.config(menu=barra_menu)
        
        menu_inicio = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
        menu_inicio.add_command(label="Salir", command=ventana.destroy)

        menu_operacion = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Operación", menu=menu_operacion)
        menu_operacion.add_command(label="Agregar receta", command=agregar_receta)
        menu_operacion.add_command(label="Ver ingredientes", command=ver_ingredientes)
        menu_operacion.add_command(label="Eliminar receta", command=eliminar_receta)

# Botón para agregar receta
btn_agregar = tk.Button(ventana, text="Agregar receta", command=agregar_receta)
btn_agregar.pack()

# Listbox para mostrar las recetas guardadas
listbox_recetas = tk.Listbox(ventana)
listbox_recetas.pack()

# Botones para ver y eliminar recetas
btn_ver = tk.Button(ventana, text="Ver ingredientes", command=ver_ingredientes) #Respuesta 1, aunque está como botón
btn_ver.pack()

btn_eliminar = tk.Button(ventana, text="Eliminar receta", command=eliminar_receta)
btn_eliminar.pack()

#Botón para salir 
salir = tk.Button(ventana, text="¡SALIR!", command=ventana.destroy)
salir.pack()


#Llamo al botón Menu 
crear_menu(ventana)


# Iniciar el bucle principal de la ventana
ventana.mainloop() #Respuesta 8, acá vemos el método que inicia el bucle principal de la aplicación

