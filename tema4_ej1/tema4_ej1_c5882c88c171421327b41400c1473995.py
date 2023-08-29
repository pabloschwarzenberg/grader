import random

def ocultar_letras(palabra,cantidad):
    largoPalabra = len(palabra)
    i = 0
    cadena = list(palabra)
    while(i < cantidad):
      posicion = random.randint(0, largoPalabra-1)
      cadena[posicion] = "_"
      i += 1
    palabra = ""
    largoCadena = len(cadena)
    i = 0
    while (i < largoCadena):
      palabra += cadena[i]
      i += 1
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    largoPalabra = len(palabra_secreta)
    palabraSecreta = list(palabra)
    i = 0
    while(i < largoPalabra):
      if(palabra_secreta[i] == letra):
        palabraSecreta[i] = letra
      i += 1
    
    palabra = ""
    i = 0
    while(i < largoPalabra):
      palabra += palabraSecreta[i]
      i += 1
    
    return palabra

if __name__ == "__main__":
    pass
         