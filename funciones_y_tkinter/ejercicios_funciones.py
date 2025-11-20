def calcular_precio_final(precio, metodo_pago):
    if metodo_pago == "tarjeta":
        recargo = precio * 0.05
        return precio + recargo
    elif metodo_pago == "efectivo":
        descuento = precio * 0.10
        return precio - descuento
    else:
        return precio

precio = float(input("Ingrese el precio del producto: "))
metodo = input("Ingrese el método de pago ('tarjeta' o 'efectivo'): ")
print("Precio final:", calcular_precio_final(precio, metodo))
