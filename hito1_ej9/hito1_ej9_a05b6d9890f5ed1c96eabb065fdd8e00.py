# Solicitar los coeficientes y términos independientes al usuario
print("Ingrese los coeficientes y los términos independientes del sistema:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
e = float(input("e = "))
f = float(input("f = "))

# Calcular el determinante
determinante = a * d - b * c

# Verificar si el sistema tiene solución única
if determinante != 0:
    # Calcular las soluciones para x e y
    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante
    
    # Imprimir las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")
