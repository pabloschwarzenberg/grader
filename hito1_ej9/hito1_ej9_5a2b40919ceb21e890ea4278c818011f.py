#Sistema de Ecuaciones
x1 = float(input("Ingrese coeficiente de x de la primera ecuacion: "))
y1 = float(input("Ingrese coeficiente de y de la primera ecuacion: "))
r1 = float(input("Ingrese resultado de la primera ecuacion: "))
x2 = float(input("Ingrese coeficiente de x de la segunda ecuacion: "))
y2 = float(input("Ingrese coeficiente de x de la segunda ecuacion: "))
r2 = float(input("Ingrese resultado de la segunda ecuacion: "))

denominador = (x1 * y2 - y1 * x2)

valorx = round((r1 * y2 - y1 * r2) / denominador ,1)
valory = round((x1 * r2 - r1 * x2) / denominador ,1)

x = "x="
y = "y="

print(x,valorx)
print(y,valory)