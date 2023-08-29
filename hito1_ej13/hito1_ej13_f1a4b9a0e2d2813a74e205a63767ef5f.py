#Factores Primos
def factores_primos(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            print(i)
    if n > 1:
        print(n)

num = int(input("Ingresa un número entero: "))
print("La descomposición de factores primos de", num, "es:")
factores_primos(num)      