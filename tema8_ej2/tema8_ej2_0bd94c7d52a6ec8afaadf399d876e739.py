def buscarTodas(a, b):
    posiciones = []
    i = 0
    for n in a:
        if a[i] == b:
            posiciones.append(str(i))
        i += 1
    cadena = " ".join(posiciones)
    return cadena

if __name__ == "__main__":
    a = input("Ingresa la palabra: ")
    b = input("Ingrese el caracter a buscar: ")
    print(buscarTodas(a, b))
           