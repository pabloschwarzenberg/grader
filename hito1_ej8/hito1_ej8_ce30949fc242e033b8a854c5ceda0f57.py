#Descomponer un número
n=eval(input("ingrese un numero de 4 digitos: "))
m=n//1000
c=(n%1000)//100
d=(n%100)//10
u=(n%10)
print(m,"M+",c,"C+",d,"D+",u,"U")