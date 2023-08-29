#Nota final
PT = 0
PI = 0
ne = 0

PT = float(input("ingrese la primera nota: "))
PI = float(input("ingrese la segunda nota: "))
NE = float(input("ingrese la tercera nota: "))
PP = float(input("ingrese la nota de presentacion  : "))
y = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("La Nota Final del curso es: ", round(y,1))