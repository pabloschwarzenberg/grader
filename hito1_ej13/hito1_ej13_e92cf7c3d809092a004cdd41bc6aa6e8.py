#Factores Primos
numero = int(input("Ingresa numero entero: "))
def factor_primo(n):
    if n == 1:
        return []
    for div in range(2, n + 1):
        if n % div == 0:
            return [div] + factor_primo(n // div)

print (factor_primo(numero))
