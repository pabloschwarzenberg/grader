text=print("Ingrese valores a, b, z de una ecuacion de la forma ax+by=z, y luego ingrese los valores de otra ecuacion de la misma forma:")

a=int(input())
b=int(input())
z=int(input())
q=int(input())
w=int(input())
e=int(input())
text1="Ecuación 1:"
text2="Ecuación 2:"
print(text1)
print(a,"x +", b,"y =",z)
print(text2)
print(q,"x +", w,"y =",e)

x=(((z*w)-(b*e))/((a*w)-(q*b)))
y=(((q*z)-(a*e))/((q*b)-(w*a)))
print("x=",x,"y=",y)
print(y)