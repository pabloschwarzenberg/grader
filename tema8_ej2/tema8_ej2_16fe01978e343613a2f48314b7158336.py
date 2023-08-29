def buscarTodas(a,b):
    lista = []
    posicion = 0
    while posicion<len(a):
        for i in a:
            if(i == b):
                lista.append(posicion)
            posicion = posicion + 1
    nueva_lista = []
    for j in lista:
        nueva_lista.append(str(j))
    cadena = " ".join(nueva_lista)
    return cadena
            

if __name__ == "__main__":
    a = input("Ingrese su string:")
    b = input("Ingrese el caracter que busca:")
    print(buscarTodas(a,b))
           