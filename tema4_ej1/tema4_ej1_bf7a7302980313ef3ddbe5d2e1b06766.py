import random
def ocultar_letras(palabra,cantidad):
    i=0
    aux=list(palabra)
    while i<=cantidad:
      pos=random.randint(1, len(palabra)-1)  
      aux[pos]="_"
      i=i+1
    return ("".join(aux)) 

def revisar_letra(palabra_secreta,palabra,letra):
    ps_=list(palabra_secreta)
    pu_=list(palabra)
    lu_=letra
    for i in range(len(palabra_secreta)):
        if(letra==ps_[i]):
            pu_[i]=lu_
    return ("".join(pu_))