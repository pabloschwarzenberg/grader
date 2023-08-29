#Descomponer un número
n=int(input("ingrese un numero de maximo cuatro cifras: "))

a=n//1000
b=n//100-(a*10)
c=n//10-(a*100+b*10)
d=n-(a*1000+b*100+c*10)

w="M +"
x="C +"
y="D +"
z="U "

print("la descomposicion del numero es: ",a,w,b,x,c,y,d,z)     