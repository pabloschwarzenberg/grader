def buscarTodas(a,b):
    pocision=""
    for x in range(len(a)):
        if len(pocision)!=0 and a[x]==b:
            pocision+=" "
        if a[x]==b:
            pocision+=str(x)
    return pocision

if __name__ == "__main__":
    a=input("cual es la palabra: ")
    b=input("cual es la letra: ")
    a.lower()
    b.lower()
    resultado=buscarTodas(a,b)
    print(resultado)

           