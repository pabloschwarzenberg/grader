a=input("ingrese primer coeficiente ec1: ")
a=float(a)
b=input("segundo coef ec1: ")
b=float(b)
c=input("tercer coef ec1: ")
c=float(c)
d=input("primer coef ec2: ")
d=float(d)
e=input("segundo coef ec2: ")
e=float(e)
f=input("tercer coef ec2: ")
f=float(f)

x=(e*c-b*f)/(a*e-b*d)
y=(a*f-d*c)/(a*e-b*d)


print("x=",x)
print("y=",y)