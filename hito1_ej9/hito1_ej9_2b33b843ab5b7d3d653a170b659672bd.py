#Sistema de Ecuaciones
      
a = float(input("Ingrese Numero para x:"))
b = float(input("Ingrese Numero para y:"))
c = float(input("Ingrese Numero para ecuacion:"))
p = float(input("Ingrese Numero para x:"))
o= float(input("Ingrese Numero para y:"))
i= float(input("Ingrese Numero para ecuacion:"))


x = (c * o - b * i) / (a * o - b * p)
y = (a * i - c * p) / (a * o - b * p    )



print("x=" +str(x) + "y="+str(y))