import random

# Lista de participantes
participantes = ["Javier", "Kalel", "samuel"]

# Definimos los parámetros de la rifa
PRECIO_BOLETA = 5000
MIN_PARTICIPANTES = 3  # Número mínimo de participantes para realizar la rifa

# Contamos cuántos boletos se vendieron
boletas_vendidos = len(participantes)

# Calculamos el dinero total recaudado
total_obtenido = boletas_vendidos * PRECIO_BOLETA

# Verificamos si hay suficientes participantes
if boletas_vendidos >= MIN_PARTICIPANTES:
    ganador_rifa = random.choice(participantes)
    print("📢 ¡La rifa ha terminado!")
    print(f"Precio de la boleta: {PRECIO_BOLETA}")
    print(f"Total obtenido: ${total_obtenido}")
    print(f"🎉 El ganador es: {ganador_rifa}")
if boletas_vendidos == MIN_PARTICIPANTES:
  print("se le dará un abono adicional de 10000 debido a que hubieron pocos participantes dentro de la rifa")
else:
    print(f"No se puede realizar la rifa, se necesitan al menos {MIN_PARTICIPANTES} participantes y solo hay {boletas_vendidos}.")
