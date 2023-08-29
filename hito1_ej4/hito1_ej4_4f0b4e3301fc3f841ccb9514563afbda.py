n=int(input('ingrese decimal: '))
binario = ''
while n // 2 != 0:
    binario = str(n % 2) + binario
    n = n // 2
resp= str(n) + binario
 
print("resultado=",resp)