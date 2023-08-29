def buscarTodas(a,b):
    a = list(a)
    resultado = []
    for i in range(len(a)):
        if b == a[i]:
            resultado.append(str(i))
    resultado = " ".join(resultado)
    return resultado        
    pass

if __name__ == "__main__":
    a = input("string base: ")
    b = input("string buscado en base: ")
    print(buscarTodas(a,b))
    pass
