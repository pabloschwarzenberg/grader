import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    palabra_actualizada = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_actualizada[i] = letra
    return "".join(palabra_actualizada)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "leon"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    letras_ocultas = random.sample(range(len(palabra)), min(cantidad, len(palabra)))
    
    while True:
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        if len(opcion) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
            letras_ocultas = random.sample(range(len(palabra)), min(cantidad, len(palabra)))
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra completa.")
            else:
                print("¡Oops! Esa no es la palabra correcta.")
            break
