def buscarTodas(a,b):
    lista = []
    pos_inicial = -1
    try:
        while True:
            pos_inicial = a.index(b, pos_inicial+1)
            lista.append(str(pos_inicial))
    except ValueError:
        print("Posiciones de la letra/palabra "+str(b)+" en la letra/palabra "+str(a)+" son : ", lista)
    n= " ".join(lista)
    return n
if __name__ == "__main__":
    a= str(input("Ingrese la palabra a:"))
    b= str(input("Ingrese la palabra b:"))
    buscarTodas(a,b)
           