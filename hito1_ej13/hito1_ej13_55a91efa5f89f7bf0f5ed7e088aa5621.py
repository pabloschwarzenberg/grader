#Factores Primos
num = int(input("Ingrese el numero que desea calcular su factor: "))#Entrada
x = 2
while(num!=1):
    if (num % x == 0):
        print(str(x)+" ")
        num = num/x
    else:
        x = x+1      