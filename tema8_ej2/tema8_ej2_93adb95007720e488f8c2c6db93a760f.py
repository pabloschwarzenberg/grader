def buscarTodas(a, b):
    indice = ""
    cont = 0
    for letra in a:
        if letra == b:
            indice = indice + str(cont) + " "
        cont += 1
    indice = indice.strip()

    return indice



if __name__ == "__main__":
    a = input("Ingrese a: ")
    a.lower()
    b = input("Ingrese b: ")
    b.lower()
    print(buscarTodas(a, b))

