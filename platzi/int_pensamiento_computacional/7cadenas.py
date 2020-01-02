my_str="Platzi"


resultado = len(my_str)#la funcion len entraga el numero de caracteres de la cadena
indice = my_str[0]#la forma de entregar indices de la cadena siempre iniciando desde el principip
indice_dos = my_str[0:5:2]#de esta forma usaremos el indice [posicion inicial:posicion final:numero de saltos]

print(my_str)
print(resultado)
print(indice)
print(indice_dos)
print("yo amo a ",my_str)
print(f"yo amo a {my_str}")