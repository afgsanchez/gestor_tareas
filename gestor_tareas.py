# Empezamos dándole un toque "gráfico" al título de la aplicación 
# usando un ascii art
print()
print("░▀█▀▒▄▀▄░▄▀▀░█▄▀░░░█▄▒▄█░█░█▄░█░█▀▄▒██▀▒█▀▄")
print("░▒█▒░█▀█▒▄██░█▒█▒░░█▒▀▒█░█░█▒▀█▒█▄▀░█▄▄░█▀▄ v.1.0.6")
print("Created by: Antonio Gutiérrez")
print("https://github.com/afgsanchez")
print()
# Creamos un bucle while el cual se ejecutará mientras no se cumpla la
# la condición que le indiquemos (salir del programa), para poder 
# trabajar con el programa sin tener  que cargarlo cada vez que ejecutamos una tarea.
while True:

# Ahora creamos el menu para la interacción con el usuario.
    print("Elije una opción: ")
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
    
    elif seleccion == "2":
        print("+-------------------------+")
        print("| Has elegido la opcion 2 |")
        print("+-------------------------+")
        print()

    elif seleccion == "3":
        print("+-------------------------+")
        print("| Has elegido la opcion 3 |")
        print("+-------------------------+")
        print()

    elif seleccion == "4":
        print("+-------------------------+")
        print("| Has elegido la opcion 4 |")
        print("+-------------------------+")
        print()

    elif seleccion == "5":
        print("+---------------------------------+")
        print("| Has elegido SALIR del programa. |")
        print("+---------------------------------+")
        print()
        print("Muchas gracias por usar TASK MINDER")
        print()
        print("░▀█▀▒▄▀▄░▄▀▀░█▄▀░░░█▄▒▄█░█░█▄░█░█▀▄▒██▀▒█▀▄")
        print("░▒█▒░█▀█▒▄██░█▒█▒░░█▒▀▒█░█░█▒▀█▒█▄▀░█▄▄░█▀▄ v.1.0.6")
        print("Created by: Antonio Gutiérrez")
        print("https://github.com/afgsanchez")
        print()
        break

    else:
        print("+--------------------------------------+")
        print("| POR FAVOR, ELIJE UNA OPCION DEL MENU |")
        print("+--------------------------------------+")
        print()
       



