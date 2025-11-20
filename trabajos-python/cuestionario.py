print("--------------------- Bienvenido al cuestionario ------------------------")
print("")
print("¿Cuántos meses tienen 28 días?")
print("A. Solo febrero")
print("B. Uno ")
print("C. Todos")
print("D. Nueve")
print("")
puntaje = 0
pregunta1 = input("Escriba su respuesta: ")
print("")
print("¿Si corres una carrera y adelantas al segundo, ¿en qué posición quedas?")
print("A. Primero")
print("B. Segundo ")
print("C. Tercero")
print("D. Último")
print("")
pregunta2 = input("Escriba su respuesta: ")
print("")
print("Si un tren eléctrico va de norte a sur, ¿hacia dónde va el humo?")
print("A. Al sur")
print("B. Al norte")
print("C. No hay humo, es eléctrico")
print("D. Hacia arriba ")
print("")
pregunta3 = input("Escriba su respuesta: ")
print("")
print("Un hombre construye una casa con todas las paredes mirando al sur. Un oso pasa por ahí. ¿De qué color es el oso?")
print("A. Marrón")
print("B. Negro")
print("C. Blanco")
print("D. Gris")
print("")
pregunta4 = input("Escriba su respuesta: ")
print("")
print("Tienes dos monedas que suman 30 céntimos, pero una de ellas no es de 10 céntimos. ¿Qué monedas tienes?")
print("A. Una de 20 y una de 10")
print("B. Dos de 15")
print("C. Dos de 10")
print("D. Una de 25 y una de 5")
print("")
pregunta5 = input("Escriba su respuesta: ")
print("")
print("Si dos personas juegan 5 partidas de ajedrez y cada una gana 3, ¿cómo es posible?")
print("A. Hicieron trampa")
print("B. Se equivocaron contando")
print("C. No jugaron entre ellas")
print("D. El resultado es imposible")
print("")
pregunta6 = input("Escriba su respuesta: ")
print("")
print("Si un mes empieza en domingo, ¿cuántos viernes 13 tendrá?")
print("A. 0")
print("B. 1")
print("C. 2")
print("D. 13")
print("")
pregunta7 = input("Escriba su respuesta: ")
print("")
print("Si 5 máquinas hacen 5 productos en 5 minutos, ¿cuánto tardarán 100 máquinas en hacer 100 productos?")
print("A. 100 minutos")
print("B. 50 minutos")
print("C. 5 minutos")
print("D. 10 minutos")
print("")
pregunta8 = input("Escriba su respuesta: ")
print("")
print("Un gallo está en la cima de un tejado inclinado. Si pone un huevo, ¿hacia qué lado caerá?")
print("A. Izquierda ")
print("B. Derecha ")
print("C. No caerá")
print("D. No caerá porque los gallos no ponen huevos ")
print("")
pregunta9 = input("Escriba su respuesta: ")
print("")
print("Si un coche rojo va a 100 km/h y otro azul va a 100 km/h, pero el rojo recorre 200 km y el azul 150 km, ¿cuál llegó primero?")
print("A. El rojo")
print("B. El azul")
print("C. Depende del tiempo de viaje")
print("D. Llegan al mismo tiempo")
print("")
pregunta10 = input("Escriba su respuesta: ")
if pregunta1 == "C":
  resp1 = "Correcto"
  puntaje +=1
else:
  resp1 = "Incorrecto"
if pregunta2 == "B":
  resp2 = "Correcto"
  puntaje +=1
else:
  resp2 = "Incorrecto"
if pregunta3 == "C":
  resp3 = "Correcto"
  puntaje +=1
else:
  resp3 = "Incorrecto"
if pregunta4 == "C":
  resp4 = "Correcto"
  puntaje +=1
else:
  resp4 = "Incorrecto"
if pregunta5 == "A":
  resp5 = "Correcto"
  puntaje +=1
else:
  resp5 = "Incorrecto"
if pregunta6 == "C":
  resp6 = "Correcto"
  puntaje +=1
else:
  resp6 = "Incorrecto"
if pregunta7 == "B":
  resp7 = "Correcto"
  puntaje +=1
else:
  resp7 = "Incorrecto"
if pregunta8 == "C":
  resp8 = "Correcto"
  puntaje +=1
else:
  resp8 = "Incorrecto"
if pregunta9 == "D":
  resp9 = "Correcto"
  puntaje +=1
else:
  resp9 = "Incorrecto"
if pregunta10 == "C":
  resp10 = "Correcto"
  puntaje +=1
else:
  resp10 = "Incorrecto"

if puntaje >=10:
  calificacion = "Gran Maestro"
elif puntaje >=8:
  calificacion = "Buen puntaje"
elif puntaje <=6:
  calificacion = "Debes poner más esfuerzo"
print("")
print("-----------------------")
print("La pregunta 1 es:",resp1)
print("La pregunta 2 es:",resp2)
print("La pregunta 3 es:",resp3)
print("La pregunta 4 es:",resp4)
print("La pregunta 5 es:",resp5)
print("La pregunta 6 es:",resp6)
print("La pregunta 7 es:",resp7)
print("La pregunta 8 es:",resp8)
print("La pregunta 9 es:",resp9)
print("La pregunta 10 es:",resp10)
print("-------------------------")
print("Tu puntuación es:",puntaje)
print(calificacion)