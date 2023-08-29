#Factores Primos
P = int(2)
num =int(input("Ingrese el número: "))

while (num != 1):
    if (num % P == 0):
        print(str(P) + " ")
        num = num / P
    else:
        P = P + 1   