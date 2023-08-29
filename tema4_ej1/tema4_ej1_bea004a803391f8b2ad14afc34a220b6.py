import random

lista = ['paralelepipedo','rocknroll','roflmao']

def ocultar_letras(palabra,cantidad):
    nuevaPalabra = list(palabra)
    x = 0
    while x != cantidad:
        i = random.randint(0,len(nuevaPalabra)-1)
        if nuevaPalabra[i] != '_':
            nuevaPalabra[i] = '_'
            x += 1
    palabra = ''.join(nuevaPalabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    palabra = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra[i] = letra
    palabra = ''.join(palabra)
    return palabra

if __name__ == "__main__":
    palabraSecreta = random.choice(lista)
    cantidad = random.randint(1,len(palabraSecreta)-1)
    print(palabraSecreta, cantidad)
    palabra = ocultar_letras(palabraSecreta, cantidad)
    print(palabra)
    for i in range(7):
        letra = input()
        palabra = revisar_letra(palabraSecreta, palabra, letra)
        print(palabra)