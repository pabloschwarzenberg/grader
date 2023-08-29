import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = len(palabra_secreta) // 2
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    
    print("Adivina la palabra secreta:")
    print(palabra_mostrada)
    
    while "_" in palabra_mostrada:
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        elif opcion == palabra_secreta:
            palabra_mostrada = opcion
        else:
            print("Opción inválida. Intenta")\