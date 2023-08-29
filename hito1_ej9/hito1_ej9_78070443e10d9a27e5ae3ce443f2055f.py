def resolver(a, b, c, d, e, f):
  x = (c*e - b*f) / (a*e - b*d)
  y = (a*f - c*d) / (a*e - b*d)
  print("x=", round(x,1))
  print("y=", round(y,1))

a=int(input("Ingrese un numero "))
b=int(input("Ingrese un numero "))
c=int(input("Ingrese un numero "))
d=int(input("Ingrese un numero "))
e=int(input("Ingrese un numero "))
f=int(input("Ingrese un numero "))

resolver(a, b, c, d, e, f)