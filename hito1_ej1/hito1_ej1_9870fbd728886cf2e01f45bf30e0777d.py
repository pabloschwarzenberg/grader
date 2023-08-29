#Nota final
PT = float(input("ingrese nota de tareas: "))
PI = float(input("ingrese nota de Interrogaciones: "))
NE = float(input("ingrese nota de Examen: "))
PP = float(input("ingrese nota de Presentacion: "))

Nota_final = round((PT*0.3 + PI*0.3 + NE * 0.3 + PP*0.1),1)
print("nota final: ", Nota_final)     