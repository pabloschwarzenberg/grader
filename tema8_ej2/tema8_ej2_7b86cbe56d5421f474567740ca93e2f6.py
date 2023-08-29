def buscarTodas(a,b):
    a.lower()
    b.lower()
    palabra = []
    for i in range(len(a)):
        if a[i] == b:
            valori = i
            palabra.append(valori)
    letra = " ".join(map(str, palabra))
    return letra
    pass

if __name__ == "__main__":
    a = input('Ingrese un texto: ')
    b = input('Ingrese una letra: ')
    print(buscarTodas(a, b))
    pass