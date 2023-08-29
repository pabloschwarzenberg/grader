def buscarTodas(a,b):
    lista = []
    for indice in range(0,len(a)):
        caracter = a[indice]
        if caracter == b:
            lista.append(str(indice))
    
    return ' '.join(lista)
        
if __name__ == "__main__":
    a = input("Ingresa un string a: ")
    b = input("Ingrese el string que desee buscar b: ")
    
    print(str(buscarTodas(a,b)))