def buscarTodas(a,b):
    L=[]
    i=0
    for letra in a:
        if letra==b:
            posicion=i
            posicion=str(posicion)
            L.append(posicion)
        i=i+1
    S=" ".join(L)
    return S
           
           
if __name__ == "__main__":
    x=input("Ingrese Frase ")
    y=input("ingrese la letra a buscar ")
    print(buscarTodas(x,y))