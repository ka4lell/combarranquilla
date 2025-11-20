lista = []

n = int(input("Cuántos números deseas ingresar? "))
for i in range(n):
    numero = int(input(f"Introduce el número {i + 1}: "))
    lista.append(numero)


while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Ver lista completa")
    print("2. Ordenar la lista")
    print("3. Quitar un número")
    print("4. Añadir un nuevo número")
    print("5. Vaciar toda la lista")
    print("6. Salir del programa")

    opcion = input("Elige una opción (1-6): ")

    match opcion:
        case "1":
            print(f"Lista actual: {lista}")

        case "2":
            lista.sort()
            print("Lista ordenada:", lista)

        case "3":
            numero_a_borrar = int(input("¿Qué número quieres quitar? "))
            if numero_a_borrar in lista:
                lista.remove(numero_a_borrar)
                print(f"Se quitó el número {numero_a_borrar}.")
            else:
                print("Ese número no está en la lista.")

        case "4":
            nuevo_numero = int(input("Escribe el número que quieres añadir: "))
            lista.append(nuevo_numero)
            print(f"Se añadió el número {nuevo_numero} a la lista.")

        case "5":
            lista.clear()
            print("La lista ha sido vaciada.")

        case "6":
            print("Gracias por usar el programa.")
            break

        case _:
            print("Opción inválida. Por favor, elige una opcion del 1 al 6.")