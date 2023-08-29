#Conversión de Decimal a Binario

numdec=int(input("ingrese un numero decimal: "))
bin(numdec)
a=int(bin(numdec)[2:])
print("resultado=",a)