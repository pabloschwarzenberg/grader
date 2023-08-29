import random
def ocultar_letras(palabra,cantidad):
    ocultar=0
    lista=[]
    while ocultar < cantidad:
        posicion=random.randint(0,cantidad-1)
        if lista.count(posicion)==0:
            lista.append(posicion)
            palabral=list(palabra)
            palabral[posicion]="_"
            palabra="".join(palabral)
            ocultar+=1
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    if (letra in palabra_secreta) ==1:
        n=0
        posiciones=[]
        while n <len(palabra):
            if palabra_secreta[n]==letra:
                posiciones.append(n)
            n+=1
        palabralista=list(palabra)
        for pos in posiciones:
            palabralista[pos]=letra
        pal="".join(palabralista)
        return(pal)
        
if __name__ == "__main__":
    pass
         