def precio_tarifa_horaria(precio, hora):
    if hora >= 22 or hora < 6:
        recargo = precio * 0.20
        return precio + recargo
    else:
        return precio

precio_tarifa = float(input("Ingrese el precio base del servicio: "))
hora = int(input("Ingrese la hora (0 a 23): "))
print("Precio con tarifa horaria:", precio_tarifa_horaria(precio_tarifa, hora))
