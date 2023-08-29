#Funcion buscarTodas
def buscarTodas(a,b):
    indices = ""

    for i in range(len(a)):
        if a[i] == b:
            indices += str(i) + " "

    indices = indices.strip()
    return indices

if name == "main":
    frase = input("Frase: ")
    letra = input("Letra: ")
    print(buscarTodas(frase,letra))