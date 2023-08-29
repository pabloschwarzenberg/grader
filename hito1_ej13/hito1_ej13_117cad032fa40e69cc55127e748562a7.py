#Factores Primosdef largest_prime_factor(n)
n=int(input("Ingrese Numero: "))
primos = []
for i in range(2,n+1):
    while (n % i == 0):
          primos.append(i)
          n = n / i
for fac in primos:
    print(fac)