#Ordenar tres números
a=eval(input("ingresar un numero"))
b=eval(input("ingresar un numero"))   
c=eval(input("ingresar un numero"))   

x= max(a,b,c)
y= min(a,b,c)
z=(a+b+c)-x-y

print(y,",",z,",",x)