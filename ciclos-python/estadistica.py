#construye un programa que, al recibir como datos el peso, la altura y el genero 
# de N personas, que pertenecen a un estado de un pais , obtenga el promedio del peso
# y el promedio de la altura, tanto la población masculina como la femenina.



comprobar =True

while comprobar == True:



    n = int(input("Ingrese la cantidad de personas a evaluar: "))

    if n >0:
        
        comprobar = False
        peso_hombre = 0
        altura_hombre = 0
        peso_mujer  = 0
        altura_mujer = 0
        cantidad_hombres = 0
        cantidad_mujeres = 0

        for i in range(n):

            peso = float(input("ingrese peso en kg: "))
            altura = float(input("ingrese altura en cm: "))
            comprobar_genero = True
            while comprobar_genero == True:
                genero = input("ingrese genero M/F: ")

        #funcion para convertir letras en mayusculas
                if genero.upper() == "M":
                    comprobar_genero = False        
                    peso_hombre += peso
                    altura_hombre += altura
                    cantidad_hombres +=1
                
                elif genero.upper() == "F": 
                    comprobar_genero = False       
                    peso_mujer += peso
                    altura_mujer += altura
                    cantidad_mujeres +=1
                
                else:
                    print("Ingrese genero correcto")

            promedio_peso_h = 0
            promedio_altura_h = 0
           
            if cantidad_hombres > 0:
                promedio_peso_h = peso_hombre / cantidad_hombres
                promedio_altura_h = altura_hombre / cantidad_hombres
           
            promedio_peso_m = 0
            promedio_altura_m = 0
           
            if cantidad_mujeres > 0:
                promedio_peso_m = peso_mujer / cantidad_mujeres
                promedio_altura_m = altura_mujer / cantidad_mujeres

            #salto de linea
            print("\nde los datos obtenidos, los promedios son: "
                "\npromedio peso hombre: ",promedio_peso_h,
                "\npromedio altura hombre: ",promedio_altura_h,
                "\npromedio peso mujer: ",promedio_peso_m,
                "\npromedio altura mujer: ",promedio_altura_m)


        else:

            print("numero ingresado es incorrecto, intente nuevamente")