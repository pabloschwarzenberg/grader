#Factores Primo     
print("introduzca el numero")
numero = int(input())
contador = 1
for divisor in range(2,numero):
    if (numero % divisor) == 0 :
        print(divisor)
        contador += 1