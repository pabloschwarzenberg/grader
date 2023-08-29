#Sistema de Ecuaciones
# Sistema de ecuaciones lineales
print("Indique los coeficientes del sistema de ecuaciones lineales: ")
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))
d = float(input("Coeficiente d: "))
e = float(input("Coeficiente e: "))
f = float(input("Coeficiente f: "))
x = (c*e - b*f)/(a*e - b*d)
y = (a*f - c*d)/(a*e - b*d)
print("Valor de la variable X: ",round(x,2))
print("Valor de la variable Y: ",round(y,2))      