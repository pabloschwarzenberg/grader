def buscarTodas(a,b):
    a = list(a)
    lista_strings = []
    for i in range (len(a)):
        if a[i] == b:
            lista_strings.append(str(i))
    lista_strings = " ".join(lista_strings)
    return lista_strings
    
    

if __name__ == "__main__":
    a = input(" ingre i1")
    b = input("ingrese 2")
    z = buscarTodas(a,b)
    print(z)
