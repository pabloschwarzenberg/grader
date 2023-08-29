#Descomponer un número
n=int(input("ingrese in numero de hasta 4 dijitos:"))

a=n%10
b=int((n-a)/10)%10
c=int((n-b)/100)%10
d=int((n-c)/1000)%10
print(d,"M +",c,"C +",b,"D +",a,"U")