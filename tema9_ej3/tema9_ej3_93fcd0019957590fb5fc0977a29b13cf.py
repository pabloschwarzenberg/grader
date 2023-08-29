def buscarTodas(a,b):
    string=""
    for i in range(len(a)):
        if a[i]==b:
            string+=str(i)+" "
    return string


if __name__=="__main__":
    a=input("ingrese palabra: ")
    b=input("letras a buscar: ")
    print(buscarTodas(a,b))