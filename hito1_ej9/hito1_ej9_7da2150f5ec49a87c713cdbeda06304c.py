a=float(input("Ingresa un numero: "))
b=float(input("Ingresa un numero: "))
c=float(input("Ingresa un numero: "))
d=float(input("Ingresa un numero: "))
e=float(input("Ingresa un numero: "))
f=float(input("Ingresa un numero: "))
x=float((e*c-b*f)/(a*e-b*d))
y=float((a*f-d*c)/(a*e-b*d))
r_x=round(x,1)
r_y=round(y,1)
print("x=",r_x,",y=",r_y)
