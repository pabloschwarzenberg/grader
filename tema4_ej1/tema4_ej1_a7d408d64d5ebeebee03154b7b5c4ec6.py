import random

lista_palabras_secretas=['obstruida','huida','marques','jamon','dominar']

def ocultar_letras(palabra,cantidad):
#contador
    k=0
    contador=[]
    while k<len(palabra):
        contador.append(k)
        k+=1
#posiciones aleatoriamente escogidas:
    i=0
    while i<cantidad:
        n=random.randint(0,len(palabra))
        if cantidad==len(palabra):
            for n in contador:
                a=palabra[n]
                palabra=palabra.replace(a,"_",1)
        if n in contador:
            contador.remove(n)
            a=palabra[n]
            palabra=palabra.replace(a,"_",1)
            i+=1
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    #contador
    k=0
    contador=[]
    while k<len(palabra):
        contador.append(k)
        k+=1
    #función en si
    if letra in palabra_secreta:
        if len(letra)==1:
            f=palabra_secreta.find(letra)
            if f in contador:
                if palabra_secreta[f]==palabra[f]:
                    k=palabra_secreta.find(letra,f+1)
                    P=list(palabra)
                    del P[k]
                    P[k:k]=[letra]
                    palabra=str(P).replace("'","").replace("[","").replace("]","").replace(", ","")
                    return palabra

                elif palabra_secreta[f]!=palabra[f]:
                    P=list(palabra)
                    del P[f]
                    P[f:f]=[letra]
                    palabra=str(P).replace("'","").replace("[","").replace("]","").replace(", ","")
                    return palabra
                    
            elif f not in contador:
                return palabra
        elif letra==palabra_secreta:
            return palabra_secreta
        else:
            return palabra
    else:
        return palabra

if __name__=="__main__":
    n=random.randint(0,len(lista_palabras_secretas)-1)
    k=lista_palabras_secretas[n]
    palabra_secreta='lepidoptero'
#Ocultar_letras:
    m=random.randint(1,len(palabra_secreta))
    palabra=ocultar_letras(palabra_secreta,m)
    print(palabra)
    i=0
    while i<7:
        letra=input()
        palabra=(revisar_letra(palabra_secreta,palabra,letra))
        print(palabra)
        if palabra==palabra_secreta:
            break
        else:
            i+=1