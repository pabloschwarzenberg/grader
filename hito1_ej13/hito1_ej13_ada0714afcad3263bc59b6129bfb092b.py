#Factores Primos
NUMERO = int(input("Ingrese un numero:"))
j=2
while j<=NUMERO:
    if NUMERO%j==0:
        print(j)
        NUMERO = NUMERO/j
    else:
        j+=1