def sumaDivisores(n, divisor = None):
    n = abs(n)
    if divisor == 0:
        return 0
    if not divisor:
        divisor = n
    divisor_valido = 0
    if (n%divisor == 0):
        divisor_valido = divisor
    suma = divisor_valido  + sumaDivisores(n  , divisor  -1 )
    return suma
print(sumaDivisores(8))
print(sumaDivisores(9))