#Factores Primos
def descomponer(n):
    for i in range(2, n+1):
        while n % i ==0:
            print(i)
            n = n / i

n =  int( input("Introduce un número para descomponer: ") )
descomponer(n)