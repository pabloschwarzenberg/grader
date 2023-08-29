#Factores Primos
a=eval(input("Ingresa un numero: "))
b = [2, 3, 5, 7, 11]
for i in b:
    if a%i==0:
        print(i)
