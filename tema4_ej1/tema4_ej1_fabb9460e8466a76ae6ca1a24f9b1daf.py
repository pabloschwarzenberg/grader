import random
def ocultar_letras(palabra,cantidad):
  N=list(palabra)
  longitud=len(N)
  Rindex=random.randrange(longitud+1)
  
  if cantidad>=longitud:
    for i in range(0,longitud):
      N[i]="_"
      i=i+1
  else:
    for i in range(0,cantidad):
     Rindex=random.randrange(longitud)
     N[Rindex]="_"
     i=i+1
  palabra="".join(N)
  return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
         