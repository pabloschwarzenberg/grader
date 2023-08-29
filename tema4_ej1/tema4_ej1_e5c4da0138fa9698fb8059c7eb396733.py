import random

def ocultar_letras(palabra,cantidad):
    palabra = list(palabra)
    escogidas = []
    i=0
    while i<cantidad:
      pos =random.randint(0,len(palabra))
      if pos not in escogidas:
        escogidas.append(pos)
        palabra[i]="_"
        i+=1
    palabra = "".join(palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    palabra = list(palabra)
    for i in range(len(palabra_secreta)):
      if palabra[i]=="_" and palabra_secreta[i]==letra:
        palabra[i]=letra
    palabra = "".join(palabra)
    return palabra

if __name__ == "__main__":
    pass
         