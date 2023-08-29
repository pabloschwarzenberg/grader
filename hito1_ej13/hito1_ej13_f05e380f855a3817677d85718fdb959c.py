#Factores Primos
def numeros(n):
    for i in range(2, n+1):
        while n% i == 0:
            n= n/i
            print(i)
n=int(input("Ingrese un valor: "))
print(numeros(n))      