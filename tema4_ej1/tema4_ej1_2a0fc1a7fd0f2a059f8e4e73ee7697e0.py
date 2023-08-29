import random

def escoger_palabra():
    palabras = ["perro", "gato", "elefante", "jirafa", "rinoceronte"]
    return random.choice(palabras)

def ocultar_letras(palabra, cantidad):
    letras_a_ocultar = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for letra in letras_a_ocultar:
        palabra_oculta[letra] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    palabra_nueva = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_nueva += letra
        else:
            palabra_nueva += palabra_oculta[i]
    return palabra_nueva

def jugar():
    palabra_secreta = escoger_palabra()
    letras_a_mostrar = random.randint(1, len(palabra_secreta)-1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_a_mostrar)
    intentos = 7
    while intentos > 0:
        print(palabra_oculta)
        letra = input("Ingresa una letra o arriesga la palabra completa: ")
        if letra == palabra_secreta:
            print("¡Felicidades, adivinaste la palabra!")
            return
        elif letra in palabra_secreta:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra)
            if "_" not in palabra_oculta:
                print(palabra_oculta)
                print("¡Felicidades, adivinaste la palabra!")
                return
        else:
            intentos -= 1
            print("Letra incorrecta. Te quedan", intentos, "intentos.")
    print("Lo siento, perdiste. La palabra era", palabra_secreta)

if __name__ == "__main__":
    jugar()