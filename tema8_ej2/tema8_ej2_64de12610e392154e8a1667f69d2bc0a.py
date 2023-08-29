def buscarTodas(a,b):
    resultado = ""
    for i in range(len(a)):
        if b == a[i]:
            resultado += str(i) + " "
    resultado_nuevo = resultado[:-1]


    return resultado_nuevo

if __name__ == "__main__":
    a = str(input("Ingrese el texto: "))
    b = str(input("Ingrese la letra a buscar: "))
    print(buscarTodas(a, b))
           