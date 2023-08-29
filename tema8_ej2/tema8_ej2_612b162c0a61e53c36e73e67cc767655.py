def buscarTodas(a,b):
    posicion=[]
    for n in range(0,len(a)):
        if a[n]==b:
            posicion.append(str(n))
    posicion=" ".join(posicion)
    return posicion
    
if __name__ == "__main__":
    a=str(input("ingrese una frase: "))
    b=str(input("ingrese la letra que quiere buscar: "))
    print(buscarTodas(a,b))