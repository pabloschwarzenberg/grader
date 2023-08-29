print("sea la forma:\n  ax+by=c\n  dx+ey=f")
a=eval(input("ingrese a: "))
b=eval(input("ingrese b: "))
c=eval(input("ingrese c: "))
d=eval(input("ingrese d: "))
e=eval(input("ingrese e: "))
f=eval(input("ingrese f: "))
detA=a*e-b*d
print(detA)
ainv=e/detA
binv=-b/detA
dinv=-d/detA
einv=a/detA
x=round((ainv*c+binv*f),1)
y=round((dinv*c+einv*f),1)
print("x=",x,"\ny=",y)
