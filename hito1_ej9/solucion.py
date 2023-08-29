a=int(input("ingrese a: "))
b=int(input("ingrese b: "))
c=int(input("ingrese c: "))
d=int(input("ingrese d: "))
e=int(input("ingrese e: "))
f=int(input("ingrese f: "))
discriminante=(a*e-d*b)
x2=(f*a-d*c)/discriminante
x1=(c-b*x2)/a
print("x=",round(x1,1),"y=",round(x2,1))
