#Sistema de Ecuaciones
x1 = float(input("Ingrese el coeficiente de x1: "))
y1 = float(input("Ingrese el coeficiente de y1: "))
n1 = float(input("Ingrese el numero real 1: "))

x2 = float(input("Ingrese el coeficiente de x2: "))
y2 = float(input("Ingrese el coeficiente de y2: "))
n2 = float(input("Ingrese el numero real 2: "))
det = x1 * y2 - x2 * y1
if det != 0:
  x = (y2 * n1 - y1 * n2) / det
  y = (x1 * n2 - x2 * n1) / det

  x_redond = round(x, 1)
  y_redond = round(y, 1)
  print("x=", x_redond)
  print("y=", y_redond)
    
else:
  print("El sistema no tiene solución única.")