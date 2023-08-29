def buscarTodas(a,b):
    c=""
    for i in range(len(a)):
        if b==a[i]:
            c+=(str(i)+" ")
    return c
if __name__ == "__main__":
    a=input("ingrese un string: ")
    b=input("ingrese el string a buscar: ")
    print(buscarTodas(a,b))


           