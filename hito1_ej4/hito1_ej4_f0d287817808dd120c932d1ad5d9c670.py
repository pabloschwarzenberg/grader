#Conversión de Decimal a Binario
num= int(input("Ingrese un numero: "))
lis=[]

while num>0:
    r=int(num%2)
    lis.append(r)
    num=(num-r)/2

binario=""
for i in lis[::-1]:
    binario=binario + str(i)

print("resultado = " + str(binario))       