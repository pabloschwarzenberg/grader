def buscarTodas(a,b):
    a.lower()
    posiciones = []
    for i in range(len(a)):
        if a[i] == b:
            posicion = i
            posiciones.append(posicion)
    palabras_comunes = " ".join(map(str, posiciones))

    pass
    return palabras_comunes
if __name__ == "__main__":
    a = input("ingrese aqui: ")
    b = input("ingrese aqui: ")
    buscar = buscarTodas(a,b)
    print(buscar)
    pass
           