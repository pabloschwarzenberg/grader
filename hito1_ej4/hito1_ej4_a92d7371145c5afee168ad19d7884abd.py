num=int(input("ingresa el numero: "))
binario = ""
while num>=2:
    binario=str(num%2)+binario
    num=num // 2
print(str("resultado=")+str(num) + str(binario)) 