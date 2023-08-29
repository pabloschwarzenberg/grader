from random import randint
def ocultar_letras(palabra,cantidad):
    palabra2=list(palabra)
    while cantidad!=0:
        g=randint(0,(len(palabra))-1)
        while True:
             if palabra2[g]=="_":
                  g=randint(0,(len(palabra))-1)
                  continue
             else:
                 palabra2[g]="_"
                 cantidad-=1
                 break
    palabra="".join(palabra2)             
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    palabra2=list(palabra)
    palabra_secreta2=list(palabra_secreta)
    lista=""
    t=0
    for mark in palabra2:
        if mark=="_":
           lista+=palabra_secreta2[t]
           t+=1
        else:
           lista+="_"
           t+=1
    lista="".join(lista)
    y=lista.find(letra)
    if y==-1:
        pass
    else:
        palabra2[y]=letra
        palabra="".join(palabra2)
        return palabra
    pass

if __name__ == "__main__":
   pass