#Factores Primos
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_rango(n):
    numeros_primos = []
    for numero in range(1, n + 1):
        if es_primo(numero):
            numeros_primos.append(numero)
    return numeros_primos

def imprimir(x, primos):
    for i in primos:
        if x%i == 0 and i != 1:
            print(i)
            imprimir(x/i, primos)
            break

n = int(input())
primos = numeros_primos_rango(n)
imprimir(n, primos)      