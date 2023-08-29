def buscarTodas(a,b):
    resultado=""
    i=0
    for i in range(len(a)):
        if str(a[i])==str(b[0]):
            resultado+=str(i)+" "
            i+=1
    return resultado

if __name__ == "__main__":
    palabra=str(input("Ingrese una frase: "))
    letra=str(input("Ingrese una letra: "))
    print(buscar_Todas(palabra,letra))
           