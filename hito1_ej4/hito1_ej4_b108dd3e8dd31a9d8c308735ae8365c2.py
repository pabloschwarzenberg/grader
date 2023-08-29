#Conversión de Decimal a Binario
numero=int(input("Ingrese un numero decimal: "))
x=numero
k=[]
while (numero>0):
    a=int(float(numero%2))
    print(a)
    k.append(a)
    numero=(numero-a)/2
k.append(0)
string=""
print(string)
for j in k[::-1]:
    string=string+str(j)
    m=int(string)*10
    w=m/10
print("resultado=", w)


