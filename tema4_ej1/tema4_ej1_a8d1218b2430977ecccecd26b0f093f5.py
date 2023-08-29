import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra_mostrada[indice] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["arquitecto","ingeniero","medico","psicologo","dentista","geologo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_a_mostrar = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_a_mostrar)
    print("Palabra secreta:", palabra_mostrada)
    
    intentos = 7
    while "_" in palabra_mostrada and intentos > 0:
        entrada = input("Ingresa una letra o la palabra completa: ")
        
        if entrada == palabra_secreta:
            print("Adivinaste la palabra!")
            break
        elif len(entrada) == 1:
            letra_ingresada = entrada.lower()
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra_ingresada)
            print("Palabra mostrada:", palabra_mostrada)
        else:
            print("palabra o letra inválida. Intenta nuevamente.")
        
        intentos -= 1
        
    if "_" not in palabra_mostrada:
        print("Adivinaste la palabra!")
    else:
        print(f"No te quedan mas intentos, la palabra era {palabra_secreta}")
