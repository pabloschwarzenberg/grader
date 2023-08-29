#Factores Primos
x = int(2)
np = int(input("Ingrese un número: "))
while(np != 1):
    if (np % x == 0 ):
        print(str(x) + "")
        np = np / x
    else:
        x = x + 1      