def buscarTodas(a,b):
    apariciones=[]
    for i in range(0,len(a)):
        if a[i]==b:
            apariciones.append(i)
    out=""
    for i in apariciones:
        out+=str(i)+" "
    out=out.strip()
    return out


if __name__ == "__main__":
    a=input("ingresa un string: ")
    b=input("ingresa lo que quieras buscar: ")
    print(buscarTodas(a,b))