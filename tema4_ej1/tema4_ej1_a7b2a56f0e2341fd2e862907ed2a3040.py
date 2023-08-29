import random
def ocultar_letras(palabra,c):
    cantidad=c+1
    listap=list(palabra)
    while cantidad > 0 and len(palabra)> cantidad:
        x=listap.index(random.choice(listap))
        if x==('_'):
              listap[x]=('_')
        else:
             listap[x]=('_')
             cantidad=cantidad-1
        
    return("".join(listap))


def revisar_letra(palabra_secreta,palabra,letra):
    q=list(palabra_secreta)
    p=list(palabra)
    if palabra_secreta==letra:
      return(palabra_secreta)
    elif palabra_secreta.find(letra)==-1:
       return -1                     
    else:
        for y in range(len(p)):
         if p[y]== '_':
           if q[y]== letra:
               p[y]=q[y]
        
        return("".join(p))

if __name__ == "__main__":
    pass
         