#Conversión de Decimal a Binario
x=int(input("Ingrese número: "))
i=x
a=str()
while i>0:
        if  i%2==1 or i==1:
            i=i//2
            a+=str(1)
        elif    i%2==0:
            i=i//2
            a+=str(0)
print("resultado="+a[::-1])