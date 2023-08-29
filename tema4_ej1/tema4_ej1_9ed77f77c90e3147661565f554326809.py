import random
def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    nueva_palabra = ""
    for i in range(len(palabra)):
        if i in indices_ocultos:
            nueva_palabra += "_"
        else:
            nueva_palabra += palabra[i]
    return nueva_palabra
def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra
if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "python", "programacion", "computadora", "libreria"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    print("Palabra secreta:", palabra_mostrada)
    while "_" in palabra_mostrada:
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            print("Palabra secreta:", palabra_mostrada)
        elif opcion == palabra_secreta:
            print("¡Felicidades! Ha adivinado la palabra.")
           
