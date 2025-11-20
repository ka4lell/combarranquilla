#clasificador de numeros

numeros_positivos = 0
numeros_negativos = 0
ceros = 0

for i in range(10):
    numero = int(input("Ingresa un numero porfavor: "))
    
    
    if numero > 0:
        numeros_positivos += 1
    elif numero < 0:
        numeros_negativos += 1
    else:
        ceros += 1
        
print("numeros postivios: ", numeros_positivos)
print("numeros negativos: ", numeros_negativos)
print("cantidad de ceros :", ceros)

