def sumar (a, b):
    return a + b

def restar (a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

print("Calculadora 3000x legendaria automatica")
print("1- sumar")
print("2- restar")
print("3- multiplicar")
print("4- dividr")


opcion_a_elegir = input("Elige una opcion de la 1 a la 4 porfavor : ")
numero_1 = float(input(" Ingrese el primer numero: "))
numero_2 = float(input(" Ingrese el segundo numero: "))

if opcion_a_elegir == "1":
    resultado = sumar(numero_1, numero_2)
    print("resultado: ", resultado)
    
elif opcion_a_elegir == "2":
    resultado = restar(numero_1, numero_2)
    print("resultado: ", resultado)
    
elif opcion_a_elegir == "3":
    resultado = multiplicar(numero_1, numero_2)
    print("resultado: ", resultado)

elif opcion_a_elegir == "4":
     if numero_2 != 0:
        resultado = dividir(numero_1, numero_2)
        print("resultado:", resultado)
     else:
        print(" no se puede dividir por cero.")
else:
    print("Opción no válida.")