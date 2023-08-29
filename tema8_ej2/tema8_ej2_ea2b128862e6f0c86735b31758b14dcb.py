def buscarTodas(a,b): #frase y letra
    a = a.lower()
    b = b.lower()
    cont=len(a)
    resultado = []
    for i in range(cont):
        if(a[i]==b):
            resultado.append(str(i))
    resultado=" ".join(resultado)
    return resultado

if __name__ == "__main__":
    frase = str(input("Ingrese la frase: "))
    letra = str(input("Ingrese la letra: "))
    print(buscarTodas(frase,letra))