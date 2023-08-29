#Conversión de Decimal a Binario
d=int(input("ingrese un numero cualquiera: "))
bi=""
while d>0:
    r=d%2
    d=d//2
    bi=str(r)+bi
print("resultado=",bi)
 