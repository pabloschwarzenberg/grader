#Nota final
PT = float(input("ingrese el promedio de notas de sus trabajos: " ))
PI = float(input("ingrese el promedio de notas de sus interrogaciones: " ))
NE = float(input("ingrese su nota de examen: " ))
PP = float(input("ingrese sel promedio de su presentaciones: " ))
Promedio = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)
print( "Su promedio final es", round (Promedio,1))   