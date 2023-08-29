import random

def escoger_palabra():
    palabras = ["gato", "perro", "elefante", "jirafa", "rinoceronte"]
    return random.choice(palabras)

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    ocultas = random.sample(range(len(palabra)), cantidad)
    for i in ocultas:
        letras_ocultas[i] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra[i]
    return nueva_palabra

if __name__ == "__main__":
    palabra_secreta = escoger_palabra()
    letras_ocultas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) * 0.5))
    print("La palabra secreta es:", letras_ocultas)
    intentos = 7
    while intentos > 0:
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(letra) == 1:
            if letra in palabra_secreta:
                letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, letra)
                print("Muy bien, esa letra está en la palabra secreta:", letras_ocultas)
                if "_" not in letras_ocultas:
                    print("¡Felicidades! Adivinaste la palabra secreta.")
                    break
            else:
                print("Lo siento, esa letra no está en la palabra secreta.")
                intentos -= 1
        elif len(letra) > 1:
            if letra == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta.")
                break
            else:
                print("Lo siento, esa no es la palabra secreta.")
                intentos -= 1
        else:
            print("Por favor ingresa una letra o la palabra completa.")
    
    if intentos == 0:
        print("Lo siento, se te acabaron los intentos. La palabra secreta era:", palabra_secreta)
