## EJERCICIO EN PYTHON FUNCIONA BIEN, AL COPIAR EL CÓDIGO ACA ME ARROJA ERROR. FAVOR REVISAR EN PYTHON Y CALIFICAR

## ENTRADA DE DATOS - PROCESO - SALIDA

## ESTRUCTURACIÓN DE FUNCIONES

import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice]= "_"
        return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada


## INVOCACIÓN FUNCIONES E IMPRESIÓN EN PANTALLA

if __name__ == "__main__":
    palabras_secretas = ["MONTAÑA", "OCEANO", "ÁRBOLES", "ANIMALES", "CIELO"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta)-1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)

    intentos = 7
    while intentos > 0:
        print("Palabra mostrada", palabra_mostrada)
        print("Intentos restantes: ", intentos)
        juego_adivinanza = input("Ingresa una letra o intenta adivinar una palabra: ")

        if len(juego_adivinanza) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, juego_adivinanza)
            if juego_adivinanza not in palabra_secreta:
                intentos -= 1
        else:
            if juego_adivinanza == palabra_secreta:
                print("Felicidades! Acertaste a la palabra!La palabra secreta es:", palabra_secreta)
                break
            else:
                intentos -= 1
                
        if "_" not in palabra_mostrada:
            print("Felicidades! Acertaste a la palabra!La palabra secreta es:", palabra_secreta)
            break


    else:
        "_" in palabra_mostrada
        print("Lo siento!! Te se acabaron los intentos. La palabra secreta era: ", palabra_secreta)