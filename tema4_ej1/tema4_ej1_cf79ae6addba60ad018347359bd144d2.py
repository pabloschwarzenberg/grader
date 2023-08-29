import random
def ocultar_letras(palabra,cantidad):
    a=len(palabra)-1
    i=0
    c=list(palabra)
    b="_"
    while i<cantidad:
        c[random.randint(0,a)]=b
        i=i+1    
    palabra="".join(c)
    return palabra
def revisar_letra(palabra_secreta,palabra,letra): # b,d,letra que tu elijes
    b=0
    if letra==palabra_secreta:
        return palabra_secreta
    else:
        while b<len(palabra_secreta):
            a=palabra_secreta.find(letra,b)
            b=b+1
            if a==-1:
                pass
            else:
                c=list(palabra)
                c[a]=letra
                palabra="".join(c)
        return palabra
if __name__ == "__main__":
    a=["ahorcado","camion","elefante","pelicano","declinacion","perpendicular","mitocondria","epsilon"]
    b=a[random.randint(0,7)]
    c=7
    if len(b)%2==0:
        e=(len(b))/2 +1
    else:
        e=len(b)+1/2 +1
    d=ocultar_letras(b,e)
    while c!=0:
        if b==d:
            print("Ha adivinado la palabra secreta: ")
            print(revisar_letra(b,d,f))
            break
        else:    
            print(d)
            f=str(input("Elija una letra: "))
            d=revisar_letra(b,d,f)
            print(revisar_letra(b,d,f))
            c=c-1
    if c==0:
        print("La palabra secreta era",b)