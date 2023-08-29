#Factores Primos
def descomponer(n):
    for f in range(2,n+1):
        while n % f == 0:
            n=n/f
            print(f)

num=int(input("inserta un numero:"))
print(descomponer(num))