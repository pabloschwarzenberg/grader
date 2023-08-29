#Sistema de Ecuaciones
print("escriba sus ecuaciones de la forma a*x+b*y=m y c*x+d*y=n:")
a=float(input("Valor de a:"))
b=float(input("Valor de b:"))
m=float(input("Valor de m:"))
c=float(input("Valor de c:"))
d=float(input("Valor de d:"))
n=float(input("Valor de n:"))
x_1= d*m-b*n
x_2= d*a-b*c
x= x_1 / x_2
if x_2==0:
    print("Sistema incongruente")
else:
    x= str(x)
y_1= c*m-a*n
y_2= c*b-a*d
y= y_1 / y_2
if y_2==0:
   print("Sistema incongruente") 
else:
    y= str(y)
print("x="+x+"")
print("y="+y+"")