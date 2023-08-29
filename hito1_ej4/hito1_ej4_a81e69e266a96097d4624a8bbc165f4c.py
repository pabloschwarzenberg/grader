#Conversión de Decimal a Binario
n = int(input("Coloque un numero"))
nb = ""
while n > 0:
    if n%2==0:
        nb = str(0)+nb
    else:
        nb = str(1)+nb
    n = n//2
print("resultado=",nb)
