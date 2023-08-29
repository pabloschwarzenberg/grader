def buscarTodas(frase,simbolo): #el que coloque 
    #len(buscarTodas)
    resultado =[]
    largo = len(frase)
    a = str

    for i in range(0, largo):
        if frase[i] == simbolo:
            resultado.append(i)
            if i == 0:
                a = str(i)
            if i > 0:
                a += " "
                a += str(i)
    print(a)
    return a
if __name__ == "__main__":
    frase =  str(input("Ingrese el texto --> "))
    simbolo =  str(input("Ingrese el caracter --> "))
    buscarTodas(frase,simbolo)
    pass