# Conversión de Decimal a Binario

num = int(input("Ingrese un numero:"))
numbin = ""

while (num>0):
    if (num%2==0):
        numbin =str(0)+numbin
    else:
        numbin =str(1)+numbin
    num = num//2
print("Resultado=", numbin)
