#Factores Primos

def prime(n):
    d = 2
    primo = True
    while n > d:
        if n % d == 0:
            primo = False
            break
        d += 1
    if primo and n > 1:
        return True
    else:
        return False

def generar_primos(max):
    n = 2
    numeros_primos = []
    while n <= max:
        if prime(n):
            numeros_primos.append(n)
        n += 1
    return numeros_primos

l = int(input('Numero: '))
resultado = generar_primos(l)
i = 0
a = 1
while i < len(resultado) and a != l:
    print(resultado[i])
    a *= l
    i += 1
