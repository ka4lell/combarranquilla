# realizar un programa que permita generar la tabla de multiplicar de un numero entero 
# positivo N, comenzando desde 1
#
# si el usuario escribe un numero incorrecto, el programa no se ejecuta.
# en cambio pregunta denuevo la información hasta q el dato ingresado sea correcto

comprobar = True

while comprobar == True:

    n = int(input("Ingrese Numero entero positivo: "))

    if n > 0:
        for i in range (1,11):

            print(n, "por" , i, "es igual a:", n*i )
            comprobar = False
    else:
        print("el numero ingresado no es correcto, intente denuevo")