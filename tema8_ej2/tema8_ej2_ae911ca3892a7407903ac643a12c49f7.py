def buscarTodas(a,b):
    posicion=0
    posiciones=""
    for i in a:
        if (i==b):
            posiciones=posiciones+str(posicion)+" "
        posicion=posicion+1
    posiciones=posiciones[:-1]
    return posiciones
    pass

if __name__ == "__main__":
    pass
    a=input("Ingrese un string a: ")
    b=input("Ingrese un string b: ")
    print(buscarTodas(a,b))