#Descomponer un número
n=int(input("ingrese un numero de 4 digitos: "))
u=n%10
c=n//100%10
d=n//10%10
m=n//1000%1000
print(m,"M","+",c,"C","+",d,"D","+",u,"U")