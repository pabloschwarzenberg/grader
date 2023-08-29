#Descomponer un número
n=int(input("Ingrese el digito a descomponer: "))
a=n//1000
b=(n//100)%10
c=(n%100)//10
d=n%10

print(a,"M + ",b,"C + ",c,"D + ",d,"U",sep="")