#Factores Primos
 def factor_primos(numero):
    i = 2
    while i <= numero:
        if numero % i == 0:
            print(i)
            numero = numero / i
        else:
            i += 1

numero = int(input())

if numero <= 1:
    print("El número debe ser mayor que 1.")
else:
    factor_primos(numero)

   