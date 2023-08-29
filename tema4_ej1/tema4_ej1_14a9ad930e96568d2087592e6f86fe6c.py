def generar_palabra():
    # Retorna una palabra al azar desde una lista de palabras
    # No se preocupe por comprender cómo esta función hace su trabajo
    from random import choice
    lista = ["pandemia", "programacion", "paralelepipedo", "equilatero", "panaderia",
             "automatizacion","camila", "comida", "tonterias", "disparos", "chile", "campeon", "qatar"]  # lista de palabras en minúsculas, sin tildes ni otros símbolos
    pala = choice(lista)
    return pala


def palabra_encriptada(palabra):
    encri = ""
    for x in palabra:
        encri += "_ "  # se cambia la letra de la palabra por un guión bajo y un espacio
    return encri


# Escriba aquí su implementación de la función verificar_letra

def verificar_letra(palabra, letra):
    for i in palabra:
        if i == letra:
            return True
    return False


# Escriba aquí su implementación de la función mostrar_letra

def mostrar_letra(palabra, encriptada, letra):
    palafinal = ""
    i = 0
    while i < len(palabra):
        if palabra[i] == letra:
            palafinal += letra
        else:
            palafinal += encriptada[2 * i]
        palafinal += " "
        i += 1

    return palafinal

# Complete aquí el programa que implementa el juego
def juego():
    palabra = generar_palabra()
    encriptada = (palabra_encriptada(palabra))
    print(encriptada)
    i = 1
    while i <= 5:
        letra = int(input("Ingrese letra o palabra: "))
        if verificar_letra(palabra, letra):
            print("acertaste!")
            print("Intento", i)
            encriptada = mostrar_letra(palabra, encriptada, letra)
            print(mostrar_letra(palabra, encriptada, letra))
        else:
            print("La letra no es parte de la palabra!!")
            print("Intento", i)
            print(mostrar_letra(palabra, encriptada, letra))

        if len(letra) > 1:

            if letra == palabra:
                print("Felicitaciones acertaste a la palabra")
                print(palabra)
                print("Fin del juego")

            else:
                print("Lo sentimos, no es la palabra oculta")
                print(palabra)
                print("Fin del juego")
            break
        if i == 5:
            print("Fin del juego")
        i += 1

# Programa principal:

print("Bienvenidos al juego del adivinador de palabras!!!")
print("dispones de 5 intentos máximos para adivinar la palabra")
juego()