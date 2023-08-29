from random import randint

def ocultar_letras(palabra,cantidad):
    while cantidad>0:
        x=randint(0,(len(palabra)-1))
        if palabra[x]!="_":
            palabra=list(palabra)
            palabra.insert(x,"_")
            palabra.pop(x+1)
            cantidad-=1
    palabra="".join(palabra)        
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    lugar=[]
    resuelto=False
    palabra_secreta=list(palabra_secreta)
    for x in range(len(palabra)):
        if palabra_secreta[x]=="_":
            lugar.append(x)
    for y in lugar:
        if letra==palabra[y] and len(letra)==1:
            letra2=palabra[y]
            palabra_secreta.pop(y)
            palabra_secreta.insert(y,letra2)
        elif letra==palabra:
            palabra_secreta=palabra
    palabra_secreta="".join(palabra_secreta)
    palabra=palabra_secreta
    return palabra


                 
         