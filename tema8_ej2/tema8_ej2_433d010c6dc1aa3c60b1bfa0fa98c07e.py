def buscarTodas(a,b):
    encontrado = ""
    x = 0
    for i in a:
        if i == b:
            encontrado = encontrado + str(x) + " "
        x = x + 1

    return encontrado[:-1]

if __name__ == "__main__":
    a = input("Ingrese una frase o palabra: ")
    b = input("Ingrese caracter a encontrar: ")

    encontrado = buscarTodas(a,b)
    print(encontrado)