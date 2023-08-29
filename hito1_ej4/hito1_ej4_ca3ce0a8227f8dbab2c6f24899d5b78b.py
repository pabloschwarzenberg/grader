#Conversión de Decimal a Binario
a = int(input("Ingrese un numero decimal: "))
b=[]
while (a > 0):
    c = int(a % 2)
    print("valor de a :", c)
    b.append(c)
    a=(a-c)/2
letra=""
for i in b[::-1]:
    letra = letra+str(i)
print("Resultado={}".format(letra))