#construye un programa que, al recibir como datos el peso, la altura y el genero 
# de N personas, que pertenecen a un estado de un pais , obtenga el promedio del peso
# y el promedio de la altura, tanto la población masculina como la femenina.




print("\n--- Bienvenido al Programa de Evaluación ---")

nombre_usuario = input("Ingresa tu nombre porfavor ")
print(f"Hola, {nombre_usuario} Empecemos la evaluación.")

n = int(input("¿Cuántas personas deseas evaluar? "))

if n > 0:
    peso_hombre = altura_hombre = peso_mujer = altura_mujer = 0
    cantidad_hombres = cantidad_mujeres = 0
    peso_saludable = 0
    contador_personas = 0
    bajo_peso = sobrepeso = peso_normal = 0

    for i in range(n):
        contador_personas += 1
        print(f"\n--- Persona {contador_personas} ---")
        peso = float(input("Ingrese peso en kg (mayor a 0): "))
        while peso <= 0:
            print("Peso inválido.")
            peso = float(input("Ingrese peso en kg (mayor a 0): "))

        altura = float(input("Ingrese altura en cm (mayor a 0): ")) / 100
        while altura <= 0:
            print("Altura inválida.")
            altura = float(input("Ingrese altura en cm (mayor a 0): ")) / 100

        genero = input("Ingrese género M/F: ").upper()
        while genero not in ("M", "F"):
            print("Género inválido.")
            genero = input("Ingrese género M/F: ").upper()

        Peso_0 = round(peso / (altura ** 2), 2)
        print(f"Peso de la persona {contador_personas}: {Peso_0}")

        if Peso_0 < 18.5:
            bajo_peso += 1
            print("Comentario: Bajo peso, tienes que echarle ganas")
        elif 18.5 <= Peso_0 <= 24.9:
            peso_normal += 1
            peso_saludable += 1
            print("Comentario: Peso saludable, perfecto")
        else:
            sobrepeso += 1
            print("Comentario: Sobrepeso, te toca ir al gym")

        if genero == "M":
            peso_hombre += peso
            altura_hombre += altura * 100
            cantidad_hombres += 1
        else:
            peso_mujer += peso
            altura_mujer += altura * 100
            cantidad_mujeres += 1

    promedio_peso_h = peso_hombre / cantidad_hombres if cantidad_hombres > 0 else 0
    promedio_altura_h = altura_hombre / cantidad_hombres if cantidad_hombres > 0 else 0

    promedio_peso_m = peso_mujer / cantidad_mujeres if cantidad_mujeres > 0 else 0
    promedio_altura_m = altura_mujer / cantidad_mujeres if cantidad_mujeres > 0 else 0

    print("\n--- Resumen de Evaluación ---")
    print(f"Personas evaluadas: {contador_personas}")
    print(f"Promedio peso hombres: {promedio_peso_h:.2f} kg")
    print(f"Promedio altura hombres: {promedio_altura_h:.2f} cm")
    print(f"Promedio peso mujeres: {promedio_peso_m:.2f} kg")
    print(f"Promedio altura mujeres: {promedio_altura_m:.2f} cm")
    print(f"Personas con peso saludable: {peso_saludable} de {n}")
    print(f"Bajo peso: {bajo_peso}, Peso normal: {peso_normal}, Sobrepeso: {sobrepeso}")

    if peso_normal == contador_personas:
        print("Felicidades, todos estan en forma")
    elif sobrepeso > 0:
        print("Recuerda cuidar tu salud")
    else:
        print("Ánimo, echale ganas")

    print(f"\nGracias por usar el programa, {nombre_usuario}!")
else:
    print("Número ingresado incorrecto, intente nuevamente.")