#Conversión de Decimal a Binario
Decimal=int(input("Ingrese un numero decimal:"))
Valor=Decimal
Valor2=[]
while (Decimal>0):
    Valor3=int(float(Decimal%2))
    Valor2.append(Valor3)
    Decimal=(Decimal-Valor3)/2
string=""
for Valor4 in Valor2[::-1]:
    string=string+str(Valor4)
print("resultado=",string)
     