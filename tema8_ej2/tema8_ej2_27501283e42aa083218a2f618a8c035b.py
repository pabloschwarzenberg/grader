def buscarTodas(a,b): 
    valor = 0 
    z = list(a)
    l = ""
    for letras in a:
        if z[valor] == b:
            x = str(valor)
            l = l + x + " "
        valor +=  1
    xd = list(l)
    lenLista = len(xd)
    del xd[lenLista - 1]
    xd = "".join(xd)
    return(xd)

if __name__ == "__main__":
    x = str(input("ingresa frase o palabra"))
    y = str(input("ingresa letra de la frase o palabra"))
    print(buscarTodas(x,y))
 
           