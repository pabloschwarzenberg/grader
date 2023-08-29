#Conversión de Decimal a Binario
x=int(input("ingrese un numero: "))
if x<=0:
    print("0")
bina=""
resto=0
while x>0:
    resto=int(x%2)
    x=int(x/2)
    bina=str(resto) + bina
print("resultado=",bina)


