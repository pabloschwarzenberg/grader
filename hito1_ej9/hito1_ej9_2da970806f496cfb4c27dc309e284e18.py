print("Introduzca numeros de tal manera que las ecuaciones sean distintas de 0 y estas no se anulen entre ellas")
print("Ecuacion_1:")
a=float(input("coeficiente que acompaña a x:"))
b=float(input("coeficiente que acompaña a y:"))
c=float(input("coeficiente libre:"))
print("Ecuacion_2:")
d=float(input("coeficiente que acompaña a x:"))
e=float(input("coeficiente que acompaña a y:"))
f=float(input("coeficiente libre:"))
g=float((c*d-a*f)/(b*d-a*e))
print("y=",g)
h=float((c*e-b*f)/(a*e-d*b))
print("x=",h)

             
      