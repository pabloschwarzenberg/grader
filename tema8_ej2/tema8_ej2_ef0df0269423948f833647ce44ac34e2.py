def buscarTodas(a,b):
    aux = ""
    contador1 = 0
    for letra in a:
        if letra == b:
            aux += str (contador1) + " "
        contador1 = contador1 + 1
    pass

    return aux [:-1]

if __name__ == "__main__":
    x = str (input ("Ingrese palabra: "))
    y = str (input ("Ingrese letra: "))
    a = buscarTodas(x,y)
    print (a)

    pass
