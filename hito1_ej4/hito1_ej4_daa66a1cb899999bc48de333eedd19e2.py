n=int(input(""))
numero_binario = 0
multiplicador = 1
while n != 0:
    numero_binario = numero_binario + n % 2 * multiplicador
    n //= 2
    multiplicador *= 10
        
print(("resultado="+str(numero_binario)))
