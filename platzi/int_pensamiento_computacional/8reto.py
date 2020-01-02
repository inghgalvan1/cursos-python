usuario_uno = input("¿quien es el usuario uno?")
usuario_dos = input("¿quien es el usuario dos?")

print(usuario_uno, "¿cual es tu edad?")
edad_usuario_uno = int(input())

print(usuario_dos, "¿cual es tu edad?")
edad_usuario_dos = int(input())

if edad_usuario_uno > edad_usuario_dos:
    print(usuario_uno, "es mayor que ", usuario_dos)
elif edad_usuario_uno < edad_usuario_dos:
    print(usuario_dos, "es mayor que",usuario_uno)
else:
    print("ambos tienen la misma edad")

