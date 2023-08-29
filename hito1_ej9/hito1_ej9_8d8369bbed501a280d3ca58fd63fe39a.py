#Sistema de Ecuaciones
print("Forma ax+by=c / dx+ey=f")
a=int(input("a>"))
b=int(input("b>"))     
c=int(input("c>"))
d=int(input("d>"))
e=int(input("e>"))
f=int(input("f>"))

#pp=a*x+b*y=c po=d*x+e*y=f x=(c-b*y)/a
print(a,"x +",b,"y =",c,"//",d,"x +",e,"y =",f)
y=(f*a-d*c)/(e*a-b)
x=(c-b*y)/a
print("x=",x)
print("y=",y)