#Factores Primos
Number = int(input("Ingrese Numero: "))
def descomponer():
    verificador = 1
    lista = []
    primos = []
    for i in range(2, Number+1):
        if Number % i == 0:
            lista.append(i)
    for n in lista:
        for i in range(2, n):
            if n % i == 0:
                primos.append(n)
    for n in primos:
        if n in lista:
            lista.remove(n)
    for number in lista:
        verificador *= number
    if verificador != Number:
        lista.append(Number//verificador)
    for i in lista:
        print(i)
descomponer()