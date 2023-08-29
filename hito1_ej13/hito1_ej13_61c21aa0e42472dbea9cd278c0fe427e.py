#Factores Primos
def EsPrimo(x):
    p = True
    for i in range(2,x):
        if x % i == 0:
            p = False
    if x == 1:
        p = False
    return p

def FactoresPrimos(x):
    a =[]
    while x > 1:
        for i in range(1,(x+1)):
            if x % i == 0 and EsPrimo(i):
                a.append(i)
                x = x // i
            elif x == 1:
             break
    return a
 
a = int ( input("Ingrese Numero a Descomponer Factorialmente: "))
b=sorted(FactoresPrimos(a))
i=0
while i < len(b):
    print(b[i])
    i=i+1
