#Conversión de Decimal a Binario
numero=int(input("Ingrese un numero para convertir a binario:"))
x=str(bin(numero))
f=x[2:len(x)]
print("resultado=",f)