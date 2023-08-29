PALABRAS_SECRETAS = ['computadora', 'programacion', 'desarrollo', 'software', 'algoritmo']


def escoger_palabra():
    return random.choice(PALABRAS_SECRETAS)


def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for letra_oculta in letras_ocultas:
        palabra_oculta[letra_oculta] = "_"
    return "".join(palabra_oculta)


def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra = ""
    for i, letra_palabra in enumerate(palabra_secreta):
        if letra_palabra == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_oculta[i]
    return nueva_palabra


if _name_ == "_main_":
    PALABRA_SECRETA = escoger_palabra()
    NUM_LETRAS_OCULTAS = int(len(PALABRA_SECRETA) / 2)
    PALABRA_OCULTA = ocultar_letras(PALABRA_SECRETA, NUM_LETRAS_OCULTAS)
    NUM_INTENTOS = 7
    letras_intentadas = []

    print(f"La palabra secreta es: {PALABRA_OCULTA}")
    while True:
        if "_" not in PALABRA_OCULTA:
            print("¡Felicitaciones, has adivinado la palabra secreta!")
            break
        elif NUM_INTENTOS == 0:
            print("Lo siento, no has adivinado la palabra secreta. ¡Inténtalo de nuevo!")
            break

        letra_ingresada = input("Ingresa una letra o si quieres arriesgarte di la palabra completa: ").lower()
        if len(letra_ingresada) > 1:
            if letra_ingresada == PALABRA_SECRETA:
                print("¡Felicitaciones, has adivinado la palabra secreta!")
                break
            else:
                print("Lo siento, la palabra ingresada no es la correcta.")
                NUM_INTENTOS -= 1

        elif letra_ingresada in letras_intentadas:
            print("Ya intentaste esa letra, por favor ingresa otra.")
            continue

        elif letra_ingresada in PALABRA_SECRETA:
            letras_intentadas.append(letra_ingresada)
            PALABRA_OCULTA = revisar_letra(PALABRA_SECRETA, PALABRA_OCULTA, letra_ingresada)
            print("Muy bien, esa letra está en la palabra secreta.")
            print(f"La palabra es: {PALABRA_OCULTA}")
        else:
            letras_intentadas.append(letra_ingresada)
            NUM_INTENTOS -= 1
            print("Lo siento, esa letra no está en la palabra secreta.")
            print(f"Te quedan {NUM_INTENTOS} intentos.")
         