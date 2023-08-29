#Conversión de Decimal a Binario
n = int(input("Ingrese un numero decimal: "))
b=" "

while n>0:
    a=n%2
    n=n//2
    b=str(a)+b

print ("Resultado=", b)      