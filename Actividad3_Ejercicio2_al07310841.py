print("Ejercicio 2: Menu de Otoño Espresso")
print("Nombre: Mariana Vallejo Hernandez")
print("Matricula: al07310841")

while True:
    print()
    print("*** Cafeteria Otoño Espresso ***")
    print("1. Ver bebidas")
    print("2. Ver postres")
    print("3. Ver horario")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print(" Neblina de Vainilla .......... $50")
        print(" Caramelo clandestino ......... $60")
        print(" Nuble dorara ................. $55")
    elif opcion == "2":
        print(" Elixir de Canela ............. $25")
        print(" Destello de Pistacho ......... $35")
        print(" Bomba de Caramelo ............ $40")
    elif opcion == "3":
        print(" Lunes a viernes: 7:00 am - 7:00 pm")
        print(" Sabados: 9:00am a 3:00pm")
    elif opcion == "4": 
        print(" ¡Gracias por visitar Otoño Espresso! ¡Hasta luego! ")

    else:
        print(" Opcion no valida, elige del 1 al 4")