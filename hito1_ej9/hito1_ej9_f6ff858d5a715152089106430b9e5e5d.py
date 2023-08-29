#Sistema de Ecuaciones
 
a = int(input("ingrese un numero a: "))
b = int(input("ingrese un numero b: "))
c = int(input("ingrese un numero c: "))
d = int(input("ingrese un numero d: "))
e = int(input("ingrese un numero e: "))
f = int(input("ingrese un numero f: "))

y = ((f*a)-(d*c))/((a*e)-(d*b))

x = (c-b*y)/a

y = round(y,1)
x = round(x,1)

print("['x=",x,", 'y=",y,"']")