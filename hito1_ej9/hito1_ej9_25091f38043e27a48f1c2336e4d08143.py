#Sistema de Ecuaciones
a=float(input("valor1"))
b=float(input("valor2"))
c=float(input("valor3"))
d=float(input("valor4"))
e=float(input("valor5"))
f=float(input("valor6"))
y=(f-((d*c)/a))/(e-((d*b)/a))
x=(c-(b*y))/a
print("x="+str(x)+",y="+str(y))      