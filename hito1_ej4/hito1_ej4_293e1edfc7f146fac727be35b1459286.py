#Conversión de Decimal a Binario
num = int(input("Num: "))
n = num
binario = ""
if n == 0:
    print("0")
else:
    while n != 0:
        bina = n % 2
        binario += str(bina)
        n = n // 2

    print(binario[::-1])