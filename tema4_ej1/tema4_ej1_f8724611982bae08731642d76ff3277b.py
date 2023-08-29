import random
def ocultar_letras(palabra,cantidad):
    n=cantidad
    a=list(palabra)
    for i in range(1,n+1):
        while True:
          k=random.choice(a)
          if k=="_":
              continue
          else:
              break
        indice=a.index(k)
        a.pop(indice)
        a.insert(indice,"_")
    return "".join(a)


def revisar_letra(palabra_secreta,palabra,letra):
    #revisar "_"
    #for i in longitud , if a[i]="_" hacemos pop(i) i insertamos en una COPIA y revisamos
    L=list(palabra)
    LS=list(palabra_secreta)
    longitud=len(palabra)
    for i in range(0,longitud):
        if L[i]=="_":
            indice=L.index("_",i)
            if LS[indice]==letra:
                L.pop(indice)
                L.insert(indice,letra)
    return "".join(L)
    
    return palabra

if __name__ == "__main__":
    pass
         