def precio_con_envio(precio_base, envio_incluido):
    if envio_incluido:
        return precio_base + 10000
    else:
        return precio_base

precio_base = float(input("Ingrese el precio base del producto: "))
envio = input("¿Incluye envío? (si/no): ").lower() == "si"
print("Precio con envío:", precio_con_envio(precio_base, envio))