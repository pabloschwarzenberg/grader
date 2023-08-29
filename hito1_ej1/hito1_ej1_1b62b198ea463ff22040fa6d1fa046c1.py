#Nota final
PT=float(input("ingrese nota de tareas:"))
PI=float(input("ingrese nota de interrogaiones:"))
NE=float(input("ingrese nota de examen"))
PP=float(input("ingrese nota de presentacion"))
k=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
k=round(k,1)
print("su promedio es:", k)