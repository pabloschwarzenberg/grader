#Aprobación de créditos
    #Conversión de Decimal a Binario
n = int(input())
i = 0
while 2**i <= n:
    i += 1
i -= 1
binario = ""
while i>=0:
    if n - 2**i >= 0:
        binario = binario + "1"
        n -= 2**i
    else:
        binario = binario + "0"
    i -= 1
print("resultado="+binario)  