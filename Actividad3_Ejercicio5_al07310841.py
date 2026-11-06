print("Ejercicio 5: El menu de tu proyecto CRUD")
print("Nombre: Mariana Vallejo Hernandez")
print("Matricula: al07310841")
print()

# Pedimos el nombre del sistema 
nombre_sistema = input("¿Como se llama tu sistema?")

#Contador de operaciones: empiezo en 0
operaciones = 0

# El menu se repite siempre; la unica salida es el break
while True:
    print()
    print("=====", nombre_sistema, "=====")
    print("1. Altas")
    print("2. Bajas")
    print("3. Cambios")
    print("4. Consultas")
    print("5. Imprimir")
    print("6. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print(" Aqui iran las ALTAS de tu proyecto")
        operaciones = operaciones + 1
    elif opcion == "2":
        print(" Aqui iran las BAJAS de tu proyecto")
        operaciones = operaciones + 1
    elif opcion == "3":
        print(" Aqui iran los CAMBIOS de tu proyeto")
        operaciones = operaciones + 1 
    elif opcion == "4":
        print(" Aqui iran las CONSULTAS de tu proyecto")
        operaciones = operaciones + 1
    elif opcion == "5":
        print(" Aqui ira IMPRIMIR de tu proyecto")
        operaciones = operaciones + 1
    elif opcion == "6":
        # Antes de salir, confirmamos 
        seguro = input("¿Seguro que quieres salir? (s/n):")

        # ¿La respuesta es IGUAL a "s"?
        if seguro == "s":
            print(" Hiciste ", operaciones, " operaciones. ¡Hasta luego!")
            # break nos saca del while 
            break
        else:
            print(" Regresando al menu... ")
    else:
        # Opcion invalida: no se cuenta como operacion 
        print(" Opcion no valida, elige del 1 al 6")