#Nota final
import math

PT=float(input("Ingrese Tareas:"))
PI=float(input("Ingresa Interrogaciones:"))
NE=float(input("Ingresa Examen:"))
PP=float(input("Ingresa Presentacion:"))

multi=0.3

uno=PT*multi
dos=PI*multi
tres=NE*multi
cuatro=PP*multi

suma=uno+dos+tres+cuatro


redondeo=int(suma)

print(float(redondeo))