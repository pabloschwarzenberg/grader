#Conversión de Decimal a Binario
x = float(input("Ingrese un numero: "))
binario = ""
while True:
    divicion = x / 2
    print("divicion =", divicion)
    resto = x % 2
    print("resto =",resto)
    x = x // 2
    print("x=", x)
    if resto == 1:
        binario += "1"
    else:
        binario += "0"
    if x < 1:
        break
print("resultado=",(binario)[::-1])

