#Conversión de Decimal a Binario
n=float(input("ingresar numero:"))
resultado=[]
while n!=0:
    digito=n%2
    real=int(digito)
    num=str(real)
    n=n//2
    resultado.append(num)

resultado.reverse()
numero="".join(resultado)
print("resultado=",numero)