#Ordenar tres números
import math
X = int(input("Ingrese un numero: "))
Y = int(input("Ingrese un segundo numero: "))
Z = int(input("Ingrese un tercer numero: "))
Ma = max(X,Y,Z)
print("el número mayor es: ", Ma)
Mi = min(X,Y,Z)
print("el número menor es: ", Mi)
D = (X + Y + Z) - Ma - Mi
print("De menor a mayor el órden es ", Mi, "," , D , ",", Ma) 
