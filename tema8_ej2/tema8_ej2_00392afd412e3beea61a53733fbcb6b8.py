def buscarTodas(a, b):
    c1 = 0
    c2 = 1
    l1 = []
    barcobasurero = []
    lgt1 = (len(a))
    lgt2 = int(lgt1)
    l2 = (' '.join(l1))

    while c1 <= lgt2:
        x = str(a.find(b, c1, c2))
        c1 = c1 + 1
        c2 = c2 + 1
        if x != "-1":
            l1.append(x)

        else:
            barcobasurero.append(x)

    return ' '.join(l1)


if __name__ == "__main__":
    p1 = str(input("Ingrese la frase o palabra: "))
    p2 = str(input("Ingrese el elemento que desea buscar e identificar de la palabra: "))

    print("Los elementos que busca se encuentran presentes en las siguientes posiciones:\n", buscarTodas(p1, p2))
