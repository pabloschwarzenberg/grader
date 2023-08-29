x = int(input("Ingresa numero: "))
def factores_primos(n):
    i = 2
    factores = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factores.append(i)
    if n > 1:
        factores.append(n)
    return factores

a = (factores_primos(x))
largo = (len(a))
if largo == 1:
    print(a[0])
if largo == 2:
    print(a[0])
    print(a[1])
if largo == 3:
    print(a[0])
    print(a[1])
    print(a[2])