a=int(input("ingrese el valore de x de la primera ecuacion:"))
b=int(input("ingrese el valore de y de la primera ecuacion :"))
c=int(input("ingrese el valore de z de la primera ecuacion :"))
d=int(input("ingrese el valore de x de la segunda ecuacion :"))
e=int(input("ingrese el valore de y de la segunda ecuacion :"))
f=int(input("ingrese el valore de z de la segunda ecuacion :"))

y=(d*c-a*f)/(d*b-a*e)
x=(c-b*((d*c-a*f)/(d*b-a*e)))/a


print("x=",x)
print("y=",y)      