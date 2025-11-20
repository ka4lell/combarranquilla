def simular_cuotas():
    total = float(input("Ingrese el monto total a pagar: "))
    num_cuotas = int(input("Ingrese el número de cuotas: "))

    cuota_base = total / num_cuotas
    total_pagado = 0

    for i in range(1, num_cuotas + 1):
        recargo = cuota_base * 0.02
        cuota_total = cuota_base + recargo
        print("Cuota", i, ":", round(cuota_total, 2))
        total_pagado += cuota_total

    print("Total pagado:", round(total_pagado, 2))

simular_cuotas()