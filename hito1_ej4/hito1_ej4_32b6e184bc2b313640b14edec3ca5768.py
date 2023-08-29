#Conversión de Decimal a Binario
n=int(input("Número a convertir: "))
new_n=n/2
resto=n%2
posicion=0
x=str()
while n>0:
    new_n=int(n/2)
    if n%2==0:
        digito=0
    else:
        digito=1
    n=new_n
    x+=str(digito)
print ("Resultado= ", x[::-1])