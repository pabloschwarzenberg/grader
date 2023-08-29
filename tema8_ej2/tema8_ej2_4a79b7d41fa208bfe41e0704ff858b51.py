def buscarTodas(a, b):
    indices = ""
    
    for i in range(len(a)):
        if str(a[i]) == str(b):
            indices += str(i)+" "

    # debemos cortar el ultimo espacio del string 
    indices = indices[:-1]
            
    return indices
    
if __name__ == "__main__":
    string=input("Ingrese frase: ")
    letra=input("Ingrese la letra que quiera encontrar: ")
    buscarTodas(string,letra)