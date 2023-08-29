#Conversión de Decimal a Binario

num = eval(input("Ingrese el Número "))
x = ""
while num > 0:
    y = str(num % 2)
    x = y + x
    num = num // 2
print("resultado=",x, sep ="")