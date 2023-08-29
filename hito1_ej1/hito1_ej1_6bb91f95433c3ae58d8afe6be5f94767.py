#Nota final
import math

PT=float(input('Ingrese el promedio de tareas: '));
PI=float(input('Ingrese el promedio de las interrogaciones: '));
NE=float(input('Ingrese la nota del examen: '));
PP=float(input('Ingrese la nota de presentación: '));
NF=round(((((3 * PT) / 10 ) + ((3 * PI) / 10) + ((3 * NE) / 10) + (PP / 10))), 1);
print('La nota final del alumno es',NF);