#Conversión de Decimal a Binario
def decimal_a_binario(n):
    if(n<0):
        return "0"
    b =""
    while(n>0):
        r = int(n % 2)
        n = int(n / 2)
        b = str(r) + b
    return b
n = int(input("ingresa un decimal: "))
b = decimal_a_binario(n)
print("resultado= ",b)