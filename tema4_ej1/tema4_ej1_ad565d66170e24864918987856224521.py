from random import randint
def ocultar_letras(palabra,cantidad):
    palabra = "tillas"
    lista = []
    palabra = list(palabra)
    while cantidad != 0:
      x = randint(1, len(palabra)-1)
      if x not in lista:
        lista.append(x)
        cantidad -= 1
        palabra[x]= "_"
    palabra = "".join(palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    z = list(palabra_secreta) 
    palabra = list(palabra)
    if letra in z:
      x = palabra_secreta.find("-")
      palabra[x] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra

         