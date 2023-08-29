import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    letras_indices = random.sample(range(len(palabra)), cantidad)
    
    for indice in letras_indices:
        letras_ocultas[indice] = "_"
    
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    
    return nueva_palabra_mostrada

palabras_secretas = ["perro", "gato", "elefante", "tigre", "jirafa"]
palabra_secreta = random.choice(palabras_secretas)
letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
intentos = 7

print("Bienvenido al juego de adivinar la palabra secreta!")
print(f"La palabra tiene {len(palabra_secreta)} letras.")

while intentos > 0:
    print(f"Palabra actual: {letras_mostradas}")
    print(f"Tienes {intentos} intentos restantes.")
    
    opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
    
    if len(opcion) == 1:
        letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        
        if opcion in palabra_secreta:
            print("¡Correcto! La letra está en la palabra.")
        else:
            print("Incorrecto. La letra no está en la palabra.")
            intentos -= 1
    else:
        if opcion == palabra_secreta:
            letras_mostradas = opcion
            break
        else:
            print("Incorrecto. Esa no es la palabra.")
            intentos -= 1

if letras_mostradas == palabra_secreta:
    print("¡Felicidades! Has adivinado la palabra secreta.")
else:
    print("Lo siento, te has quedado sin intentos.")
    print(f"La palabra secreta era: {palabra_secreta}")
