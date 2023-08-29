def buscarTodas(a,b):
    posiciones = []
    posicion = 0

    while posicion != -1:
        posicion = a.find(b, posicion)
        if posicion != -1:
            posiciones.append(posicion)
            posicion += 1
            salida = [str(integer) for integer in posiciones]
            string = " ".join(salida)
            

    return string

if __name__ == "__main__":
    a=input("ingrese string a: ")
    b=input("ingrese string b: ")

    salida = buscarTodas(a, b)

    print(str(salida))
           