#Conversión de Decimal a Binario
num=int(input("Ingrese un numero decimal: "))
x=num
k=[]
while (num>0):
    a=int(float(num%2))
    k.append(a)
    num=(num-a)/2
string=""
for j in k[::-1]:
    string=string+str(j)
print("resultado=%s"%(string))