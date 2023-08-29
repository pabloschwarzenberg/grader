a= eval(input("Ingrese un número:"))
b= eval(input("Ingrese un número:"))
c= eval(input("Ingrese un número:"))
d= eval(input("Ingrese un número:"))
e= eval(input("Ingrese un número:"))
f= eval(input("Ingrese un número:"))   
   
determinante = a*e - b*d

if determinante != 0:
  x = (c*e - b*f) / determinante
  y = (a*f - c*d) / determinante
  round(x,1)
  round(y,1)

  print(x,y)
  
else:
  print(None, None)



