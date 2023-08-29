def buscarTodas(a,b):
    string=""
    for i in range(len(a)):
        if a[i]==b:
            string+=str(i)+(" "+"")
    return (string)
    pass
if __name__ == "__main__":
    b=input("ingrese la letra: ")
    a=input("palabra a buscar: ")
    print(buscarTodas(a,b))
    pass