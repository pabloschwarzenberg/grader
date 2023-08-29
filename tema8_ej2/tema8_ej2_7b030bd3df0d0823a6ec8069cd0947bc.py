def buscarTodas(a,b):
    lista1 = list(a)
    lista2 = list(b)
    #lista1 = lista1[1:-1]
    #lista2 = lista2[1:-1]
    lista3 = []
    for i in range(len(lista1)):
        if(lista1[i] == lista2[0]):
            string = i
            lista3.append(str(string))
            lista3.append(" ")
    resultado = "".join(lista3)
    print(resultado)
    resultado = resultado.strip()
    return resultado
    
if __name__ == "__main__":
    a = input("Ingresa una frase: ")#tres tristes tigres
    b = input("Ingresa una letra presente en la frase anterior: ")#t
    resultado = buscarTodas(a,b)