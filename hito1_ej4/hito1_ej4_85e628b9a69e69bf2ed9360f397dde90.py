#Conversión de Decimal a Binario
a=int(input("Ingrese un número: "))
while a>1:
    b=a%2
    a=a//2
    if b!=0:
        print(1)
    else:
        print(0)
print(1)
