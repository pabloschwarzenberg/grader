def buscarTodas(a,b):
    lista_frase = []
    suma = ""

    for n in a:
        lista_frase.append(n)
        
    
    for j in range(0, len(lista_frase)):
        if lista_frase[j] == b:
           suma += str(j) + " "
    contador = suma.strip()
    return contador
    pass 
    



if __name__ == "__main__":
    a = input("Ingrese la frase: ")
    b = input("Ingrese la letra que desea buscar en la frase: ")

    print(buscarTodas(a,b))
    pass