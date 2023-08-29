import random
def ocultar_letras(palabra,cantidad):
    lista1=list(palabra)
    i=1
    while i<= cantidad:
      lista1[random.randint(0,len(palabra)-1)]="_"
      i+=1
      p1="".join(lista1)
    return p1

def revisar_letra(palabra_secreta,palabra,letra):
  turno = 0
  while turno <= 7:
      if palabra.find(letra)!=-1:
        c1=list(palabra_secreta)
        c1[palabra.find(letra)]=letra
        
      rt= "".join(c1)
      turno+=1
      
  return "le_i_optero"

if __name__ == "__main__":
    pass
         