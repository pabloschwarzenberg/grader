import random
def ocultar_letras(palabra,cantidad):
    count=0
    cantidad_letras= len(palabra)
    for x in range(1,cantidad):
        count=count +1
        palabra[random.randint(0,cantidad_letras)]== "_"*1
        if count == cantidad:
            return palabra
          
def revisar_letra(palabra_secreta,palabra,letra):
    x= palabra_secreta.find(letra)
    if x>=0:
        palabra[x]==letra
    return palabra
         