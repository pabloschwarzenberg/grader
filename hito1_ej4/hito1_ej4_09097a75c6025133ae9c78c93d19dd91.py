print("Conversión de Decimal a Binario")
x=int(input("Introdusca un numero decimal: "))
bi=""
while x!=0:
    x_1=x%2
    x=x//2
    bi=str(x_1)+bi
print("resultado=",bi)