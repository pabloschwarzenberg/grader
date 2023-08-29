from random import randint

def ocultar_letras(palabra,cantidad):
    lista=list(palabra)
    for i in range(1,4):
        palabra=palabra.replace(lista[randint(1,len(lista))],"_")
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):#palabra_secreta = original
    if len(letra)>1:
        if letra==palabra_secreta:
            palabra=palabra_secreta
            return palabra
        else:
            return palabra
    elif len(letra)==1:
        palabrasecreta_lista=list(palabra_secreta)
        palabra_lista=list(palabra) #palabra con ____
        for i in range(0,len(palabra)):
            if letra == palabrasecreta_lista[i]:
                palabra_lista[i]=letra
        palabra="".join(palabra_lista)
        return palabra
    else:
        return palabra

if __name__ == "__main__":
    lista_palabras=["hola","ahorcado","paralelepipedo","convergente","salida","lampara","terodactilo","programacion","introduccion","ingenieria","calculo","schwarzenberg","lepidoptero"]
    a=lista_palabras[randint(1,len(lista_palabras)-1)]
    b=ocultar_letras(a,4)
    print(b)
    for k in range(1,7):
        res=input("Ingrese una letra: ")
        b=revisar_letra(a,b,res)
        print(b)
        if b==a:
            print("Ganaste!")
            break

