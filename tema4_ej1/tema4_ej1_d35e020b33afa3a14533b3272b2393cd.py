from random import randint
def ocultar_letras(palabra,cantidad):
    largo=len(palabra)
    palabra_secreta1=[]
    i=0
    j=0
    while i<largo:
        palabra_secreta1.append(palabra[i])
        i=i+1
    while j<cantidad:
        h=randint(0,largo)
        palabra_secreta1.insert(h,"_")
        if h+1<largo:
            palabra_secreta1.pop(h+1)
        else:
            palabra_secreta1.pop(h-1)
        j=j+1
    palabra_secreta= "".join(palabra_secreta1)
    return palabra_secreta
def revisar_letra(palabra,palabra_secreta,letra):
    palabra=list(palabra)
    palabra_secreta=list(palabra_secreta)
    if palabra.count(letra)==0:
        return palabra_secreta
    else:
        if palabra_secreta.count(letra)==0:
            #ACA PUEDE IR UN WHILE 
            palabra_secreta.insert(palabra.index(letra),letra)
            palabra_secreta.pop(palabra.index(letra)+1)
            return palabra_secreta
        else:
            if palabra.count(letra)>1:
                n=palabra.index(letra)
                if palabra_secreta[n]==palabra[n]:
                    n=n+1
                    palabra_secreta.insert(palabra.index(letra,n),letra)
                    palabra_secreta.pop(palabra.index(letra,n)+1)
                else:
                    palabra_secreta.insert(palabra.index(letra),letra)
                    palabra_secreta.pop(palabra.index(letra)+1)
        palabra_secreta="".join(palabra_secreta)
        return palabra_secreta


if __name__ == "__main__":
    pass
         