import random
palabras=["casa","helicoptero","transantiago","pelicula","sabores"]
miss="_"
elegida=random.choice(palabras)
m=len(elegida)
cant=random.randint(1,(m-1))

def buscarTodas(a,b):
    miss="-"
    l=[]
    nueva_a=[]
    for elemento in a:
        nueva_a.append(elemento)
    veces=nueva_a.count(b)
    for i in range (veces):
        posicion=nueva_a.index(b)
        l.append(posicion)
        nueva_a[posicion]=miss
    return l

def ocultar_letras(palabra,cantidad):
    p=""
    newpalabra=[]
    n=len(palabra)
    l=[]
    for i in palabra:
        newpalabra.append(i)
    for o in range (cantidad):
        r=random.randint(0,(n-1))
        while (r in l)==True:
            r=random.randint(0,(n-1))
        newpalabra[r]=miss
        l.append(r)
    return p.join(newpalabra)

def revisar_letra(palabra_secreta,palabra,letra):
    p=""
    newpalabra_secreta=[]
    newpalabra=[]
    for h in palabra_secreta:
        newpalabra_secreta.append(h)
    for j in palabra:
        newpalabra.append(j)
    posiciones=buscarTodas(palabra_secreta,letra)
    for i in posiciones:
            newpalabra[i]=newpalabra_secreta[i]
    return p.join(newpalabra)

if __name__ == "__main__":
    word=ocultar_letras(elegida,cant)
    print(word)
    for y in range (7):
        guess=input("Adivine letra: ")
        jaja=revisar_letra(elegida,word,guess)
        word=jaja
        print(jaja)
        if jaja==elegida:
            break