#Factores Primos
n = int(input("Ingrese un número entero: "))
def descomponer(n):
    primos= []

    for i in range(2,n+1):
        while n % i == 0:
            primos.append(i)
            n = n / i
            resultado = "\n".join([str(sublista) for sublista in primos])
    return resultado
print(descomponer(n))





        