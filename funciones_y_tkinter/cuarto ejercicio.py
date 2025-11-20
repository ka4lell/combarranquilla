numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))


tabla = []


for i in range(1, 11):
    resultado = numero * i
    tabla.append(f"{numero} x {i} = {resultado}")


print("Tabla de multiplicar del", numero)
for linea in tabla:
    print(linea)