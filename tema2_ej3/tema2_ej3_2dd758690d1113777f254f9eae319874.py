def perfecto(a):
    def divisores(numero):
        resultado=[]
        n=2
        while n<numero:
            if numero%n == 0:
                resultado.append(n)
            n = n+1
        return resultado
        print(resultado)
        
    b = divisores(a)

    def suma(lista):
        sum=0
        for i in range(0,len(lista)):
            sum = sum + lista[i]
        return sum

    print("")
    print("La suma de los divisores de",a, "son:",suma(b))

    print("")
    if suma(b) == a:
        print("El número",a,"es un número perfecto.")
    else:
        print("El número",a,"NO es un número perfecto.")

a = int(input("Ingrese número:"))

perfecto(a)
