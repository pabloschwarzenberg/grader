def decimal_binario(n):
   
    binario = []
    while n > 0:
        binario.append(str(n % 2))
        n //= 2
    binario.reverse()
    return ''.join(binario)
n=int(input("ingrese numero="))
print("resultado=", decimal_binario(n))



