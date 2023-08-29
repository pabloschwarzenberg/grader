import random
def ocultar_letras(palabra_secreta,cantidad):
  listaSecreta=list(palabra_secreta)
  for i in range(1,cantidad+1):
    posicion=random.randint(0,len(palabra_secreta)-1)
    listaSecreta[posicion]="_"
  palabra_secreta="".join(listaSecreta)
  return palabra_secreta

def revisar_letra(palabra_secreta, palabra, letra):
  x=list(palabra)
  y=list(palabra_secreta)
  for i in range(0,len(y)):
    if y[i]==letra:
        x[i]=letra
            
  return "".join(x)

if __name__ == "__main__":
    pass
         