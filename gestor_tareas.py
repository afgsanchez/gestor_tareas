# Empezamos creando una lista de tareas vacia para que el usuario
# pueda ir añadiendo tareas.
tareas = []

# Vamos a ir creando las funciones segun las opciones que tendrá
# disponible el usuario. Las definimos al principio para que sean
# accesible cuando las llamemos.

# Definimos la función 1. Agregar una tarea, que añade una tarea a la 
# lista en forma de diccionario.
def agregar_tarea(tarea):
    tareas.append({"descripcion": tarea, "completada": False })

# Definimos la función 2. Listar tareas, para ello creamos un bucle
# for que recorrerá la lista de tareas y nos las mostrará en pantalla.
def listar_tareas():
    if tareas:
        for i, tarea in enumerate(tareas):
            if tarea["completada"]:
                estado = "Completada"
            else:
                estado = "Pendiente"
            print(f"{i + 1}. {tarea['descripcion']} - {estado}")
    else:
        print("Todas las tareas estan completadas.")

# Definimos la función 3. Completar una tarea, para ello verificamos
# si la posicion de la tarea seleccionada está entre la posición 0 y el 
# total de tareas de la lista. Si es correcto marcamos la tareas como
# completada. Si la tarea no está en una posición valida, mostramos
# un mensaje de error.
def marcar_completada(posicion):
    if 0<= posicion < len(tareas):
        tareas[posicion]["completada"] = True
    else:
        print("Error!!\nLa tarea no existe en la lista de tareas!!")

# Definimos la función 4. Eliminar una tarea, para ello hacemos casi
# lo mismo que en la función 3, solo que en este caso en lugar de
# marcarla como completada, usamos el metodo "del" para eliminarla.
def eliminar_tarea(posicion):
    if 0<= len(tareas):
        del tareas[posicion]
    else:
        print("Error!!\nLa tarea no existe en la lista de tareas!!\nNo se puede eliminar!")



# Vamos a darle un toque "gráfico" al título de la aplicación 
# usando un ascii art
print()
print("░▀█▀▒▄▀▄░▄▀▀░█▄▀░░░█▄▒▄█░█░█▄░█░█▀▄▒██▀▒█▀▄")
print("░▒█▒░█▀█▒▄██░█▒█▒░░█▒▀▒█░█░█▒▀█▒█▄▀░█▄▄░█▀▄ v.1.0.3")
print("Created by: Antonio Gutiérrez")
print("https://github.com/afgsanchez")
print()
# Creamos un bucle while el cual se ejecutará mientras no se cumpla la
# la condición que le indiquemos (salir del programa), para poder 
# trabajar con el programa sin tener  que cargarlo cada vez que ejecutamos una tarea.
while True:

# Ahora creamos el menu para la interacción con el usuario.
    print(".------------------.")
    print("| Elije una opcion |")
    print("'------------------'")
    print()
    print("1. Agregar una tarea.")
    print("2. Listar tareas.")
    print("3. Completar una tarea.")
    print("4. Eliminar una tarea.")
    print("5. Salir de TASK MINDER.")
    print()

# Creamos el input para que el usuario elija una de las opciones.
    seleccion = input("Selecciona una opción: ")
    print()

# Aqui creamos lo que sucede cuando el usuario elija una de las opciones.
    if seleccion == "1":
        print("+-------------------------+")
        print("| Has elegido la opcion 1 |")
        print("+-------------------------+")
        print()
        # Ahora le pedimos la tarea al usuario.
        tarea = input("Escribe una breve descripción de la tarea: ")
        print()
        # Aquí llamamos a la funcion 1 para que añada a la lista
        # la descripcion que nos acaba de dar el usuario.
        agregar_tarea(tarea)
        # Si ha tenido exito mostramos un mensaje de confirmación
        print("Tarea añadida a la lista con éxito!")
        print("\n")


    
    elif seleccion == "2":
        print("+-------------------------+")
        print("| Has elegido la opcion 2 |")
        print("+-------------------------+")
        print()
        print("Aquí tienes el listado tareas.")
        print()
        # Ahora llamamos a la funcion 2 que es la de listar las tareas
        # que hemos ido almacenando
        listar_tareas()
        print("\n")

    elif seleccion == "3":
        print("+-------------------------+")
        print("| Has elegido la opcion 3 |")
        print("+-------------------------+")
        print()
        # Mostramos la lista de tareas para que sea facil elegir.
        listar_tareas()
        print()
        # Vamos a intentar marcar la tarea que el usuario nos indique
        # como completada. Si el usuario nos marca un numero de tarea
        # que no existe, nos muestra un mensaje de error.
        posicion = input("¿Qué número de tarea que quieres completar?: ")
        print()
        
        try:
            posicion = int(posicion) - 1 #Aqui debemos convertir la entrada
                                         # de string a entero.
            marcar_completada(posicion) # llamamos a la funcion 3 que nos
                                        # marcará la tarea como completada.
            print()
            print("Tarea marcada como completada!")
            print("\n")
        # Ahora manejamos en error en caso de entrada inválida.
        except ValueError:
            print("Ese número de tarea no existe!")
            print()
        # Y si la posición de la tarea no es válida tambien lo indicamos
        except IndexError:
            print("La posición de la tarea en la lista no es válida!")
            print()
            

    elif seleccion == "4":
        print("+-------------------------+")
        print("| Has elegido la opcion 4 |")
        print("+-------------------------+")
        print()
        # Mostramos la lista de tareas para que no se equivoque al
        # elegir la tarea a eliminar.
        listar_tareas()
        print()
        # Aqui ponemos el codigo para eliminar una tarea de la lista.
        print("¡¡ATENCION!! Esta acción no se puede revertir!")
        print()
       
        posicion = input("¿Qué número de tarea que quieres eliminar?: ")
        print()
        try:
            posicion = int(posicion) - 1 #Aqui debemos convertir la entrada
                                         # de string a entero.
            # Ahora llamamos a la funcion 4 que nos elimnará la tarea
            # que le pasemos en el parámetro posicion.
            eliminar_tarea(posicion)
            print("Tarea ", posicion + 1, " eliminada!")


            # Ahora vamos a manejar los errores de forma similar a
            # la opción anterior, pero nos mostrará los errores que 
            # nos de el sistema, no los mensajes que le hayamos programado.
        except (ValueError, IndexError) as fallo:
            print(fallo)

    elif seleccion == "5":
        print("+---------------------------------+")
        print("| Has elegido SALIR del programa. |")
        print("+---------------------------------+")
        print()
        print("Muchas gracias por usar TASK MINDER")
        print()
        print("░▀█▀▒▄▀▄░▄▀▀░█▄▀░░░█▄▒▄█░█░█▄░█░█▀▄▒██▀▒█▀▄")
        print("░▒█▒░█▀█▒▄██░█▒█▒░░█▒▀▒█░█░█▒▀█▒█▄▀░█▄▄░█▀▄ v.1.0.3")
        print("Created by: Antonio Gutiérrez")
        print("https://github.com/afgsanchez")
        print()
        break

    else:
        print("+--------------------------------------+")
        print("| POR FAVOR, ELIJE UNA OPCION DEL MENU |")
        print("+--------------------------------------+")
        print()
       



