#Factores Primos
n = int(input("ingrese numero: "))
x = int(2)
while n != 1:
    if (n % x ==0):
        print(str(x))
        n = n / x
    else:
        x = x + 1