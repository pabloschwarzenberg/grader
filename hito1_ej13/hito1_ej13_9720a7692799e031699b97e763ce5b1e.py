n = eval(input("ingrese un numero: " ))
i = 2
factores = [ ]
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        factores.append(i)
if n > 1:
    factores.append(n)
    for factor in factores:
        print(factor)