import random

def escoger_palabra():
    palabras = ["perro", "gato", "tortuga", "elefante", "jirafa"]
    palabra = random.choice(palabras)
    return palabra

def ocultar_letras(palabra, cantidad):
    ocultas = set()
    while len(ocultas) < cantidad:
        idx = random.randint(0, len(palabra)-1)
        ocultas.add(idx)
    palabra_oculta = list(palabra)
    for idx in ocultas:
        palabra_oculta[idx] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_nueva = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_nueva[i] = letra
    return ''.join(palabra_nueva)

if __name__ == "__main__":
    palabra_secreta = escoger_palabra()
    palabra_mostrada = ocultar_letras(palabra_secreta, len(palabra_secreta)//2)
    print(f"Adivina la palabra:{palabra_mostrada}")
    intentos = 7
    while intentos > 0:
        letra = input("Ingresa una letra o arriesgate a decir la palabra completa: ")
        if len(letra) > 1:
            if letra == palabra_secreta:
                print("¡Felicidades, has adivinado la palabra!")
                break
            else:
                print("La palabra que has ingresado no es correcta.")
                intentos -= 1
        else:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
            print(f"Adivina la palabra: {palabra_mostrada}")
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades, has adivinado la palabra!")
                break
            intentos -= 1
            if intentos == 0:
                print(f"Lo siento, has perdido. La palabra era {palabra_secreta}.")
            else:
                print(f"Te quedan {intentos} intentos.")