import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra
    return "".join(nueva_palabra_mostrada)

palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas", "larva"]
palabra_secreta = random.choice(palabras_secretas)
letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))

intentos = 7
adivinada = False

print("¡Bienvenido al juego de adivinar la palabra secreta!")
print("La palabra tiene", len(palabra_secreta), "letras ocultas:", letras_mostradas)

while intentos > 0:
    if "_" not in letras_mostradas:
        adivinada = True
        break
    
    print("Tienes", intentos, "intentos restantes.")
    entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ").lower()
    
    if len(entrada) == 1:
        letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, entrada)
        print("Palabra:", letras_mostradas)
    elif entrada == palabra_secreta:
        adivinada = True
        break
    else:
        print("¡Intento incorrecto!")
    
    intentos -= 1

if adivinada:
    print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
else:
    print("¡Has agotado tus intentos! La palabra secreta era:", palabra_secreta)

         