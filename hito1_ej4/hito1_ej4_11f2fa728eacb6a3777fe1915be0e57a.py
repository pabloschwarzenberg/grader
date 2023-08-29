#Conversión de Decimal a Binario
n = int(input("ingrese un numero :"))
contador = 2
#print(n%2)
res=0
num=[]
while n!=0:
    res=n%2
    n=n//2
    num.append(str(res))
res=""
contador=len(num)-1
while contador>=0:
    res=res+num[contador]
    contador=contador-1
print("resultado=",int(res))    