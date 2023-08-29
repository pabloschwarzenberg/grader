#Factores Primos
x = int(2)
num = int(input("Ingrese el numero: "))
while(num != 1):
    if (num % x == 0 ):
        print(str(x) + "")
        num = num / x
    else:
        x = x + 1
