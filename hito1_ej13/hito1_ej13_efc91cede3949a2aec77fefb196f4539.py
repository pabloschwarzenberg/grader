"""
16.- Crea un programa que imprima la descomposición de factores primos de un número.
Tu programa recibirá como entrada un número entero y debe imprimir cada factor primo del
número en una línea separada. Por ejemplo para el número 22 debiera imprimir:
2
11
"""

numero = int(input("Número: "))
posibles_factores = []

for n in range(2, numero):
    factor_primo = True
    for i in range(2, n):
        if n%i == 0:
            factor_primo = False
    if factor_primo:
        posibles_factores.append(n)

numero_dividido = numero
i = 0
while numero_dividido > 1:
    factor = posibles_factores[i]
    if numero_dividido%factor == 0:
        numero_dividido = numero_dividido/factor
        print(factor)
    else:
        i += 1