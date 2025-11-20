nombre_completo = input("Ingrese su nombre: ")
num_doc = int(input("Ingrese su número de documento: "))
confirm_doc = int(input("Confirme su número de documento: "))

# el signo != significa "distinto de" o "no es igual a"
if num_doc != confirm_doc:
    print("Los números de documento no coinciden.")
else:
    print("Documento confirmado.")

    # Listas para guardar información de los productos
    nombres_productos = []
    cantidades = []
    valores_unitarios = []
    totales_sin_descuento = []
    totales_con_descuento = []

    agregar = "r"

    while agregar.lower() == "r":
        producto = input("Nombre del producto: ")
        cantidad = int(input("Cuántas unidades desea llevar: "))
        valor = int(input("Cuál es el valor del producto: "))

        total = cantidad * valor
        descuento = total * 0.15
        total_con_desc = total - descuento

        # se agregan todos esos datos a las listas
        nombres_productos.append(producto)
        cantidades.append(cantidad)
        valores_unitarios.append(valor)
        totales_sin_descuento.append(total)
        totales_con_descuento.append(total_con_desc)

        agregar = input("Desea agregar otro producto (r/n): ")

    # se mustra un resumen de la compra
    print("\nResumen de la compra")
    suma_total = 0
    for i in range(len(nombres_productos)):
        print("\nProducto", i + 1)
        print("Producto a llevar:", nombres_productos[i])
        print("Cantidad:", cantidades[i])
        print("Valor unitario:", valores_unitarios[i])
        print("Total sin descuento:", totales_sin_descuento[i])
        print("Total con descuento (15%):", totales_con_descuento[i])
        suma_total += totales_con_descuento[i]

    print("\nTotal general a pagar:", suma_total)
    print("Gracias por su compra,", nombre_completo)