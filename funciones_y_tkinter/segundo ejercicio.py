Lista_compras = []

producto = input("Agrega un producto (escribe 'fin' para terminar): ")

while producto != "fin":
    Lista_compras.append(producto)
    producto = input("agrega otro producto (escribe 'fin' para terminar): ")
    

print("Tu lista de compras es la siguiente: ")
for item in Lista_compras:
    print(item)