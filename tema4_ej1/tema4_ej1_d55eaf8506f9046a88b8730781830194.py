import random
def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    i=0
    while i<=cantidad:
      j=random.randint(0,len(palabra)-1)
      palabra[j]="_"
      i=i+1
    palabra=".l.".join(palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta=list(palabra_secreta)
    palabra=list(palabra)
    i=0
    while i<len(palabra):
      if palabra_secreta[i]==letra:
        palabra[i]=palabra_secreta[i]
      i=i+1
    palabra="".join(palabra)
    return palabra

if __name__ == "__main__":
    pass
         