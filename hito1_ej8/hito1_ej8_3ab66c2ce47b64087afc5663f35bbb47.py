#Descomponer un número
n=int(input("Ingrese número"))
a=(n//1000)
b=(n%1000)//100
c=(n%100)//10
d=(n%10)

print(a,"M +",b,"C +",c,"D +",d,"U")
