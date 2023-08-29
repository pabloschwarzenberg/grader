def b(n):
    binario = ''
    while n // 2 != 0:
        binario = str(n % 2) + binario
        n = n // 2
    return str(n) + binario
   
numero = int(input())
print("resultado=",b(numero))
