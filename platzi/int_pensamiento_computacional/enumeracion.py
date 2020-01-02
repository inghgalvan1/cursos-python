objetivo = int(input("ingresa un numero entero: "))
respuestas = 0

while respuestas**2 < objetivo:
    print(respuestas)
    respuestas += 1

if respuestas**2 == objetivo:
    print(f"la raiz cuadrada de {objetivo} es {respuestas} ")

else:
    print(f"{objetivo} no tiene raiz cuadrada")