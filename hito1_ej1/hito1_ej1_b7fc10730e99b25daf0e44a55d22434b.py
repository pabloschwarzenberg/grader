#Nota final
pt=float(input("ingrese nota de tareas:"))
pi=float(input("ingrese nota de interroagciones:"))
ne=float(input("ingrese nota de examen:"))
pp=float(input("ingrese nota de presentacion:"))

nota_final=pt * 0.3 + pi * 0.3 + ne * 0.3 + pp * 0.1

print("su nota final es:")
print(round(nota_final, 1))   