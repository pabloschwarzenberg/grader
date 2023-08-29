#Conversión de Decimal a Binario
def decimal_a_binario(n):
             if n <=0:
                          return
             binario = ""
             while n >0:
                          residuo = int(n % 2)
                          n = int(n / 2)
                          binario = str(residuo) + binario
             return binario
n = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(n)
print("resultado =", binario)