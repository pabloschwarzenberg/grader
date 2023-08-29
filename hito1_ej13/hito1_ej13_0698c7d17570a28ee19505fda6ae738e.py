#Factores Primos
x = int(2)
numoeri = int(input("Ingrese el numero: "))
while(numoeri != 1):
    if (numoeri % x == 0 ):
        print(str(x) + "")
        numoeri = numoeri / x
    else:
        x = x + 1      