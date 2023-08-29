def buscarTodas(a, b):
    resultado = ""
    indice = 0
    while indice < len(a):
        if a[indice:indice+len(b)] == b:
            resultado += str(indice) + " "
        indice += 1
    return resultado.strip()

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    indices = buscarTodas(a, b)
    print("Apariciones de", b, "en", a, ":", indices)

           