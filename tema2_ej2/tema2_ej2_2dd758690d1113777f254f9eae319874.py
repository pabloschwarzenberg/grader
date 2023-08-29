def amigos(a,b):
    def divisores(numero):
        resultado=[]
        n=2
        while n<numero:
            if numero%n == 0:
                resultado.append(n)
            n = n+1
        return resultado
        print(resultado)

    c = divisores(a)
    d = divisores(b)

    def suma(lista):
        sum=0
        for i in range(0,len(lista)):
            sum = sum + lista[i]
        return sum

    print("")
    print("La suma de los divisores de",a, "son:",suma(c))
    print("La suma de los divisores de",b, "son:",suma(d))

    print("")
    if suma(c) == suma(d):
        print("Los números",a,"y",b,"son números amigos.")
    else:
        print("Los números",a,"y",b,"NO son números amigos.")

a = int(input("Ingrese número:"))
b = int(input("Ingrese número:"))

amigos(a,b)
