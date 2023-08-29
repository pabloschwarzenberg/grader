# Importar el módulo random para generar números aleatorios
import random

# Definir una función que oculte algunas letras de una palabra
def ocultar_letras(palabra, cantidad):
    # Crear una lista con las posiciones de las letras de la palabra
    posiciones = list(range(len(palabra)))
    # Mezclar la lista de posiciones
    random.shuffle(posiciones)
    # Tomar las primeras cantidad posiciones de la lista
    posiciones = posiciones[:cantidad]
    # Crear una lista con las letras de la palabra
    letras = list(palabra)
    # Reemplazar las letras en las posiciones escogidas por "_"
    for i in posiciones:
        letras[i] = "_"
    # Unir las letras en una sola cadena y retornarla
    return "".join(letras)

# Definir una función que revise si una letra existe en la palabra secreta y la reemplace en la palabra con letras ocultadas
def revisar_letra(palabra_secreta, palabra, letra):
    # Crear una lista con las letras de la palabra con letras ocultadas
    letras = list(palabra)
    # Recorrer la palabra secreta y comparar cada letra con la letra ingresada
    for i in range(len(palabra_secreta)):
        # Si la letra coincide, reemplazar el "_" por la letra en la misma posición
        if palabra_secreta[i] == letra:
            letras[i] = letra
    # Unir las letras en una sola cadena y retornarla
    return "".join(letras)

# Definir una función que implemente el juego de adivinar una palabra secreta
def juego():
    # Crear una lista con palabras secretas
    palabras = ["lepidoptero", "ornitorrinco", "hipopotamo", "espeleologia", "criptografia"]
    # Escoger aleatoriamente una palabra secreta de la lista
    palabra_secreta = random.choice(palabras)
    # Escoger aleatoriamente cuántas letras mostrar de la palabra secreta, entre 1 y la mitad de la longitud de la palabra
    cantidad = random.randint(1, len(palabra_secreta) // 2)
    # Ocultar algunas letras de la palabra secreta usando la función correspondiente
    palabra = ocultar_letras(palabra_secreta, cantidad)
    # Inicializar el número de intentos con 0
    intentos = 0
    # Imprimir las instrucciones del juego
    print("Bienvenido al juego de adivinar una palabra secreta.")
    print("Tienes hasta 7 intentos para adivinar la palabra.")
    print("Puedes ingresar una letra o arriesgarte a decir la palabra completa.")
    print("La palabra secreta es:")
    print(palabra)
    # Repetir el juego hasta que se adivine la palabra o se acaben los intentos
    while intentos < 7 and palabra != palabra_secreta:
        # Pedir al usuario que ingrese una letra o una palabra
        entrada = input("Ingresa una letra o una palabra: ")
        # Si la entrada es una sola letra, revisar si existe en la palabra secreta usando la función correspondiente
        if len(entrada) == 1:
            letra = entrada.lower()
            palabra = revisar_letra(palabra_secreta, palabra, letra)
            print("La palabra es:")
            print(palabra)
        # Si la entrada es una palabra completa, compararla con la palabra secreta
        elif len(entrada) > 1:
            palabra_ingresada = entrada.lower()
            # Si la palabra ingresada es igual a la palabra secreta, actualizar la palabra a
         