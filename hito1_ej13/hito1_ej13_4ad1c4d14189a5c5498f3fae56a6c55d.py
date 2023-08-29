#Factores primos
print('** Factores Primos **')

def es_primo(numero):
    if numero == 1:
        return False
    for i in range(2,numero):
        if (numero%i) == 0:
            return False
    return True

n = int(input('Ingrese el número: '))
lista = []
while n!= 1:
    for i in range(2,n+1):
        if es_primo(i) and (n%i == 0):
            lista.append(i)
    mult = 1
    for i in lista:
        mult = mult*i
    if mult == n:
        break
    else:
        n = n//mult
        if es_primo(n):
            lista.append(n)
            break
        else:
            continue

lista.sort()
for i in lista:
    print(i)
