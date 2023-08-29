#Factores Primos
n = int(input("Ingrese un número: "))

def descomponer(c):
    primo = []

    for i in range(2, c + 1):
        while c % i == 0:
            primo.append(i)
            c = c / i
            print(i)

    return primo
    
descomponer(n)