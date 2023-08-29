def buscarTodas(a, b):
    final = ""
    a_1 = list(a)
    pos = -1
    for i in range(0, a_1.count(b)):
        pos = a_1 .index(b, pos+1)
        final = final + str(pos) + " "

    return final.strip()

    pass


if __name__ == "__main__":
    a = input("Ingrese un texto: ")
    b = input("Ingrese un texto a buscar: ")
    print(buscarTodas(a, b))

    pass
           