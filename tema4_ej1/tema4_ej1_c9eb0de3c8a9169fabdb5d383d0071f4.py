import random

def escoger_palabra(palabras_secretas):
    return random.choice(palabras_secretas)

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

def jugar_adivina_palabra():
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = escoger_palabra(palabras_secretas)
    cantidad_letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, cantidad_letras_ocultas)

    intentos_restantes = 7

    while intentos_restantes > 0:
        print(palabra_mostrada)
        print(intentos_restantes)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra.")
            return

        if len(opcion) == 1:
            letra = opcion[0]
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)

            if letra not in palabra_secreta:
                intentos_restantes -= 1

        else:
            print("La opción ingresada no es válida.")

    print(palabra_secreta)

if __name__ == "__main__":
    jugar_adivina_palabra()