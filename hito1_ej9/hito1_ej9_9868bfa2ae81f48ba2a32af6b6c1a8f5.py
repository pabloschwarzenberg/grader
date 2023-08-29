#Sistema de Ecuaciones
n=eval(input("Ingrese un numero: "))
x=eval(input("Ingrese un numero: "))
y=eval(input("Ingrese un numero: "))

a=min(n,x,y)
c=max(n,x,y)
b=(n+x+y)-a-c

print(a,",",b,",",c)      