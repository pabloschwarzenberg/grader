import random

palabra = ["LEPIDOTTERO"]

palabra = list(random.choice(palabra))

letras_todas = []
fallos = 1

resultado = []

for i in range(len(palabra)):
    resultado.append("_")

while True:
    print("palabra secreta")

    print("    ", end= " ")
    for i in resultado:
        print(i,end=" ")

    if resultado == palabra:
        break
    if fallos > 7:
        print("la palabra era: ", "".join(palabra))
        break

if __name__ == "__main__":

while True:
letra_usuario_sin_formato = input("entraga una letra: ")
letra_usuario = letra_usuario_sin_formato.upper()
    if len(letra_usuario) !=1:
        print("introduce una letra")
    elif letra_usuario in letras_todas:
        print("Esa letra ya la has dicho")
    elif letra_usuario not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
        print("Introduce una letra")
    else:
        letras_todas.append(letra_usuario)
        break

for i in range(len(palabra)):
    if palabra[i] == letra_usuario:
        resultado[i] = letra_usuario

    if letra_usuario not in palabra:
        fallos += 1