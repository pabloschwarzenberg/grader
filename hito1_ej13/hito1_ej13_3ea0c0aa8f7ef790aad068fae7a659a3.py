#Factores Primos
def descomponer(n):
    for i in range(2, n+1):
        while n % i == 0:
            n= n/i
            print (i)

num= int(input("Numero a descomponer "))

print(descomponer(num))            
