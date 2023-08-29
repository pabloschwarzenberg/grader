def buscarTodas(a,b):
    indices = ""

    for i in range(len(a)):
        if a[i] == b:
            indices += str(i) + " "

    indices = indices.strip()
    return indices

if __name__ == "__main__":
    frase = input("Frase: ")
    letra = input("Letra: ")
    print(buscarTodas(frase,letra))