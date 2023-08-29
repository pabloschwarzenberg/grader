import random
def ocultar_letras(palabra,cantidad):
    palabra_list=list(palabra)
    largo=len(palabra)
    r=0
    while r<=cantidad:
      p=random.randrange(largo)
      palabra_list[p]="_"
      r+=1
    palabra="".join(palabra_list)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    ind=palabra_secreta.find(letra,11)
    palabra_list=list(palabra)
    palabra_list[ind]=letra
    palabra="".join(palabra_list)
    return palabra
