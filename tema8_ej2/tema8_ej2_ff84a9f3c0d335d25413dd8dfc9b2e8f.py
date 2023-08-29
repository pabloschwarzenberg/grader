def buscarTodas(a,b):
    coincidencias=""
    for i in range(len(a)):
        if a[i]==b:
            coincidencias=coincidencias+"{0} ".format(str(i))
    coincidencias=coincidencias.strip()
    return coincidencias

if __name__ == "__main__":
    a=input("Ingrese la frase: ")
    b=input("Ingrese letra que desea buscar: ")
    a=a.lower()
    b=b.lower()
    print(buscarTodas(a,b))

