#Factores Primos
a = int(2)
b = int(input("Ingrese el numero: "))
while(b != 1):
    if (b % a == 0 ):
        print(str(a) + "")
        b = b/a
    else:
        a =a + 1     