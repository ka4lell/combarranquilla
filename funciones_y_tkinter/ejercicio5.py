def evaluar_calificaciones(calificaciones):
    aprobados = 0
    for nota in calificaciones:
        if 0 <= nota <= 100:
            if nota >= 60:
                aprobados += 1
    return aprobados

notas = input("Ingrese las calificaciones separadas por comas (ej: 70,45,88): ")
lista_notas = [int(n.strip()) for n in notas.split(",")]
print("Cantidad de estudiantes aprobados:", evaluar_calificaciones(lista_notas))