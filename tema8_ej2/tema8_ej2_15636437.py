def buscarTodas(a,b):
    miss="-"
    l=""
    nueva_a=[]
    for elemento in a:
        nueva_a.append(elemento)
    veces=nueva_a.count(b)
    for i in range (veces):
        posicion=str(nueva_a.index(b))
        l+=posicion+" "
        posicion=int(posicion)
        nueva_a[posicion]=miss
    return l.strip()

if __name__ == "__main__":
    cosa1=input("Frase principal: ")
    cosa2=input("Frase que se quiere encontrar: ")
    print(buscarTodas(cosa1,cosa2))
