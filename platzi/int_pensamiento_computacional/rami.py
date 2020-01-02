print("ingrese dos numeros")

num_uno = int(input("ingresa el primer numero"))
num_dos = int(input("ingresa el segundo numero"))

if num_uno > num_dos:
    print("el numero", num_uno, "es mas grande que el ", num_dos)
elif num_uno < num_dos:
    print("el numero", num_dos, "es mas grande que el ", num_uno)
else:
    print("ambos numero son iguales")