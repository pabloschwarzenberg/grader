import random
def ocultar_letras(palabra,cantidad):
    cantidad=int(cantidad)
    palabral=list(palabra)
    n=1
    posiciones=[]
    while n<=cantidad:
        p=random.randint(0,len(palabra)-1)
        if p in posiciones:
            continue
        else:
            palabral[p]="_"
            posiciones.append(p)
            n+=1
            continue
    palabra="".join(palabral)
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    palabral=list(palabra)
    palabrals=list(palabra_secreta)
    n=0
    for i in palabrals:
        if i==letra:
            k=palabrals.index(letra)
            palabral[n]=letra
            n+=1
            continue
        else:
            n+=1
            continue
    palabra="".join(palabral)
    return palabra