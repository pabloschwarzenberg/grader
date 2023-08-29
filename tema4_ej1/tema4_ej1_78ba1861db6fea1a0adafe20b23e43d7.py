import random

def ocultar_letras(palabra, cantidad):
    indices = []
    for i in range(len(palabra)):
        indices.append(i)

    while cantidad > 0:
        indice = random.choice(indices)
        indices.remove(indice)
        nueva_palabra = ""
        i = 0
        for letra in palabra:
            if i == indice:
                nueva_palabra += "_"
            else:
                nueva_palabra += letra
            i += 1

        palabra = nueva_palabra
        cantidad -= 1
    
    return palabra
        
def revisar_letra(palabra_secreta, palabra, letra):
    indice = 0
    nueva_palabra = ""
    for caracter in palabra:
        if letra == palabra_secreta[indice].lower():
            nueva_palabra += palabra_secreta[indice]
        else:
            nueva_palabra += caracter
        indice += 1

    if letra == palabra_secreta.lower():
        nueva_palabra = palabra_secreta
    
    return nueva_palabra

if __name__ == "__main__":
    lista_palabras = ["Futbol", "Argentina", "Lolsito", "Gato", "Manzana", "Perro", "Juguete", "Mundo"]
    palabra_secreta = random.choice(lista_palabras)
    cantidad_ocultar = random.randint(1, len(palabra_secreta))
    palabra = ocultar_letras(palabra_secreta, cantidad_ocultar)
    print("Adivina la palabra!\n")
    print(palabra)
    intentos = 1
    juego_ganado = False
    while intentos <= 7 and not juego_ganado:
        letra = input("\nLetra: ").lower()
        palabra = revisar_letra(palabra_secreta, palabra, letra)
        if palabra == palabra_secreta:
            juego_ganado = True
        else:
            print(palabra)
            intentos += 1

    if juego_ganado:
        print("\nGANASTE! La palabra era:", palabra_secreta)
    else:
        print("\nGame over. Se te acabaron los intentos. La palabra era:", palabra_secreta)