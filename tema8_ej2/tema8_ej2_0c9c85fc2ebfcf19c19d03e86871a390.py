def buscarTodas(a, b):
    largo = int(len(a))
    i=0
    cantidad=""

    while i < largo:
        if a[i]==b:
            cantidad+=str(i) +" "
        i+=1

    return cantidad.strip()


if __name__ == "__main__":
    a = input("Ingrese palabra: ")
    b = input("Ingrese letra: ")

    c=buscarTodas(a,b)

    print(c)
