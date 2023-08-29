#Factores Primos
def FactoresPrimo(n):
    factor = 2
    while factor <= n:
        if not (n % factor != 0):
            n /= factor
            print(factor)
            #print(n)
        else:
            factor += 1
            #print(factor)
            #print(n)

x = int(input("Ingrese un numero: "))
FactoresPrimo(x)
