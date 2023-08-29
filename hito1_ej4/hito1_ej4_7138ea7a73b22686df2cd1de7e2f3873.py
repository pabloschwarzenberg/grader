#Conversión de Decimal a Binario
numero = int(input("Ingrese un numero decimal: "))
x=n
k=[]
while (numero>0):
    a=int(float(numero%2))
    print("valor de a :",a)
    k.append(a)
    n=(numero-a)/2

string=""
for j in k[::-1]:
    string=string+str(j)
print("El numero decimal %d equivale en binario a %s" %(x, string))      