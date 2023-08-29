
def buscarTodas(a, b):
    lista = []
    for i in range(len(a)):
        if a[i] == b:
            lista.append(str(i))
    if len(lista) == 0:
        return "no existe"
    return " ".join(lista)

if __name__ == "__main__":
    a = input("Ingrese a: ")
    b = input("Ingrese b: ")
    resultado = buscarTodas(a, b)
    print(resultado)
           