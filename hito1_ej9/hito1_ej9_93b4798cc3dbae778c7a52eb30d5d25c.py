#sistema de ecuaciones

a=float(input("x1:"))
b=float(input("y1:"))
e=float(input("c1:"))

c=float(input("x2:"))
d=float(input("y2:"))
f=float(input("c2:"))



print(a,"x +",b,"y =",e)
print(c,"x +",d,"y =",f)

x= (e*d-b*f)/(a*d-b*c)
y= (a*f-e*c)/(a*d-b*c)

print("x=",x)
print("y=",y)
      