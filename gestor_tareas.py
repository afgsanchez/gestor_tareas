# Importamos las librerias necesarias para guardar la lista en un 
# archivo externo y para codificar el contenido del archivo en base64.
import base64
import json

# Definimos la clase TaskManager
class TaskManager:

    # Definimos el constructor
    def __init__(self):
        self.tareas = [] # Iniciamos una lista vacia

    # Definimos el metodo 1. Agregar una tarea, que añade una tarea a la 
    # lista en forma de diccionario.
    def agregar_tarea(self, tarea):
        self.tareas.append({"descripcion": tarea, "completada": False})
    
    # Definimos el metodo 2. Listar tareas, para ello creamos un bucle
    # for que recorrerá la lista de tareas y nos las mostrará en pantalla.
    def listar_tareas(self):
        if self.tareas:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{i + 1}. {tarea['descripcion']} - {estado}")
        else:
            print("Todas las tareas están completadas.")
     
    # Definimos el metodo 3. Completar una tarea, para ello verificamos
    # si la posicion de la tarea seleccionada está entre la posición 0 y el 
    # total de tareas de la lista. Si es correcto marcamos la tareas como
    # completada. Si la tarea no está en una posición valida, mostramos
    # un mensaje de error.
    def marcar_completada(self, posicion):
        if 0 <= posicion < len(self.tareas):
            self.tareas[posicion]["completada"] = True
            print("¡Tarea marcada como completada!")
            print()
        else:
            print("Error!!\n¡La tarea no existe en la lista de tareas!")

    # Definimos el metodo 4. Eliminar una tarea, para ello hacemos casi
    # lo mismo que en la función 3, solo que en este caso en lugar de
    # marcarla como completada, usamos el metodo "del" para eliminarla.
    def eliminar_tarea(self, posicion):
        if 0 <= posicion < len(self.tareas):
            del self.tareas[posicion]
            print("¡Tarea eliminada!")
            print()
        else:
            print("Error!!\n¡La tarea no existe en la lista de tareas!\n¡No se puede eliminar!")


    # Creamos la funcion que nos creará en archivo y codificará en base64
    def guardar_archivo(self, nombre_archivo):
        # Aqui le decimos que abra el archivo en modo 'w' (write, escritura)
        with open(nombre_archivo, 'w') as archivo:
            # Ahora coge la lista de tareas (self.tareas) y la codifica en base64
            tareas_codificadas = base64.b64encode(json.dumps(self.tareas).encode()).decode()
            # Ahora escribe la lista de tareas codificada en el archivo.
            archivo.write(tareas_codificadas)


    # Creamos la funcion que nos cargará el archivo, lo decodificará deasde base64
    # y lo cargará en la lista (self.tareas)
    def cargar_desde_archivo(self, nombre_archivo):
        # Aqui abre el archivo en modo lectura 'r'
        try:
            with open(nombre_archivo, 'r') as archivo:
            # AHora lee el archivo codificado y lo carga en la variable tareas_codificadas
                tareas_codificadas = archivo.read()
            # Ahora decodifica desde base64 la variable tareas_codificadas, lo que resulta
            # en la lista legible en formato diccionario y la carga en la lista de tareas (self.tareas)
                self.tareas = json.loads(base64.b64decode(tareas_codificadas.encode()).decode())
                print("Lista de tareas cargada!\nElige la opción 2 para ver las tareas.")
        except FileNotFoundError:
                print("Error!\nEl archivo no existe o no está en el mismo directorio que el programa!")
        except (ValueError, IndexError) as petada1:
                print(petada1)

# Ahora creamos el objeto task_manager de la clase TaskManager()

task_manager = TaskManager()

# Vamos a darle un toque "gráfico" al título de la aplicación 
# usando un ascii art
print()
print("░▀█▀▒▄▀▄░▄▀▀░█▄▀░░░█▄▒▄█░█░█▄░█░█▀▄▒██▀▒█▀▄")
print("░▒█▒░█▀█▒▄██░█▒█▒░░█▒▀▒█░█░█▒▀█▒█▄▀░█▄▄░█▀▄ v.1.0.7")
print("Created by: Antonio Gutiérrez")
print("https://github.com/afgsanchez")
print()

# Creamos un bucle while el cual se ejecutará mientras no se cumpla la
# la condición que le indiquemos (salir del programa), para poder 
# trabajar con el programa sin tener  que cargarlo cada vez que ejecutamos una tarea.

while True:

# Ahora creamos el menu para la interacción con el usuario.
    print("====================================================")
    print()
    print(".------------------.")
    print("| Elije una opción |")
    print("'------------------'")
    print()
    print("1. Agregar una tarea.")
    print("2. Listar tareas.")
    print("3. Completar una tarea.")
    print("4. Eliminar una tarea.")
    print("5. Guardar tareas en un archivo.")
    print("6. Cargar archivo de tareas.")
    print("7. Salir de TASK MINDER.")
    print("8. Ayuda")
    print()

# Creamos el input para que el usuario elija una de las opciones.
    seleccion = input("Selecciona una opción: ")
    print()

# Aqui creamos lo que sucede cuando el usuario elija una de las opciones.
# Segun lo que elija el usuario iremos llamando a los metodos correspondientes.

    if seleccion == "1":
        print("+-------------------------+")
        print("| Has elegido la opción 1 |")
        print("+-------------------------+")
        print()
# Ahora le pedimos la tarea al usuario.
        tarea = input("Escribe una breve descripción de la tarea: ")
        print()
# Aquí llamamos al metodo 1 para que añada a la lista
# la descripcion que nos acaba de dar el usuario.
        task_manager.agregar_tarea(tarea)
# Si ha tenido exito mostramos un mensaje de confirmación
        print("¡Tarea añadida a la lista con éxito!")
        print("\n")

    elif seleccion == "2":
        print("+-------------------------+")
        print("| Has elegido la opción 2 |")
        print("+-------------------------+")
        print()
        print("Aquí tienes el listado de tareas:")
        print()
# Ahora llamamos al metodo 2 que es la de listar las tareas
# que hemos ido almacenando
        task_manager.listar_tareas()
        print("\n")

    elif seleccion == "3":
        print("+-------------------------+")
        print("| Has elegido la opción 3 |")
        print("+-------------------------+")
        print()
# Mostramos la lista de tareas para que sea facil elegir.
        task_manager.listar_tareas()
        print()
# Vamos a intentar marcar la tarea que el usuario nos indique
# como completada. Si el usuario nos marca un numero de tarea
# que no existe, nos muestra un mensaje de error.
        posicion = input("¿Qué número de tarea quieres completar?: ")
        print()

        try:
#Aqui debemos convertir la entrada de string a entero.
            posicion = int(posicion) - 1
# llamamos al metodo 3 que nos marcará la tarea como completada.
            task_manager.marcar_completada(posicion)
            print("\n")
# Ahora manejamos el error en caso de entrada inválida.
        except ValueError:
            print("¡Ese número de tarea no existe!\n")
# Y si la posición de la tarea no es válida tambien lo indicamos
        except IndexError:
            print("¡La posición de la tarea en la lista no es válida!\n")

    elif seleccion == "4":
        print("+-------------------------+")
        print("| Has elegido la opción 4 |")
        print("+-------------------------+")
        print()
# Mostramos la lista de tareas para que no se equivoque al
# elegir la tarea a eliminar.
        task_manager.listar_tareas()
        print()
# Aqui ponemos el codigo para eliminar una tarea de la lista.
        print("¡¡ATENCIÓN!! Esta acción no se puede revertir!\n")
        posicion = input("¿Qué número de tarea quieres eliminar?: ")
        print()

        try:
#Aqui debemos convertir la entrada de string a entero.
            posicion = int(posicion) - 1
# Ahora llamamos al metodo 4 que nos elimnará la tarea
# que le pasemos en el parámetro posicion.
            task_manager.eliminar_tarea(posicion)
            print("\n")
# Ahora vamos a manejar los errores de forma similar a
# la opción anterior, pero nos mostrará los errores que 
# nos de el sistema, no los mensajes que le hayamos programado.
        except (ValueError, IndexError) as fallo:
            print(fallo)
    
    elif seleccion == "5":
        print("+-------------------------+")
        print("| Has elegido la opción 5 |")
        print("+-------------------------+")
        print()
        # Pedimos al usuario un nombre para el archivo que vamos a crear.
        nombre_archivo = input("Dale un nombre al archivo (no es necesario extensión): ")
        # Llamamos a la función guardar_archivo con el argumento del nombre de archivo
        # para que nos lo cree. 
        task_manager.guardar_archivo(nombre_archivo)
        # Informamos al usuario que se ha creado el archivo.
        print("Archivo guardado y codificado!\n")

    elif seleccion == "6":
        print("+-------------------------+")
        print("| Has elegido la opción 6 |")
        print("+-------------------------+")
        print()
        # Pedimos al usuario un nombre del archivo a cargar.
        nombre_archivo = input("Escribe el nombre del archivo para cargar: ")
        # Llamamos a la función cargar_desde_archivo con el argumento del nombre de archivo
        # para que nos lo cargue en la lista de tareas.
        task_manager.cargar_desde_archivo(nombre_archivo)
        # Informamos al usuario que se ha cargado el archivo.
                      

    elif seleccion == "7":
        print("+---------------------------------+")
        print("| Has elegido SALIR del programa. |")
        print("+---------------------------------+")
        print()
        print("¡Muchas gracias por usar TASK MINDER!")
        print()
        print("░▀█▀▒▄▀▄░▄▀▀░█▄▀░░░█▄▒▄█░█░█▄░█░█▀▄▒██▀▒█▀▄")
        print("░▒█▒░█▀█▒▄██░█▒█▒░░█▒▀▒█░█░█▒▀█▒█▄▀░█▄▄░█▀▄ v.1.0.7")
        print("Created by: Antonio Gutiérrez")
        print("https://github.com/afgsanchez")
        print()
        break

    elif seleccion == "8":
        print("+-----------------------------------------+")
        print("|             GUÍA DE USO                 |")
        print("+-----------------------------------------+")
        print("Bienvenido a Task Minder! Este programa te permite gestionar tus tareas de manera simple y eficiente.")
        print("A continuación, te mostramos las opciones disponibles:")
        print()
        print("1. Agregar una tarea: Permite añadir una nueva tarea a la lista.")
        print("2. Listar tareas: Muestra todas las tareas almacenadas, indicando su estado (completada o pendiente).")
        print("3. Completar una tarea: Marca una tarea como completada.")
        print("4. Eliminar una tarea: Elimina una tarea de la lista.")
        print("5. Guardar tareas en un archivo: Guarda todas las tareas en un archivo codificado en base64.")
        print("    - Al elegir esta opción, se te pedirá que escribas un nombre para el archivo.")
        print("    - Asegúrate de escribir un nombre único y sin extensión.")
        print("    - No debes usar palabras reservadas del sistema, por ejemplo 'data'.")
        print("6. Cargar archivo de tareas: Carga las tareas desde un archivo previamente guardado.")
        print("    - Al elegir esta opción, se te pedirá que escribas el nombre del archivo a cargar.")
        print("    - Asegúrate de escribir el nombre exacto del archivo, sin extensión.")
        print("7. Salir de Task Minder: Cierra el programa.")
        print("8. Ayuda: Muestra esta guía de uso.")
        print()
        print("¡Esperamos que disfrutes usando Task Minder para organizar tus tareas!")
        print("+-----------------------------------------+")
        print()


    else:
        print("+--------------------------------------+")
        print("| POR FAVOR, ELIJE UNA OPCIÓN DEL MENÚ |")
        print("+--------------------------------------+")
        print()