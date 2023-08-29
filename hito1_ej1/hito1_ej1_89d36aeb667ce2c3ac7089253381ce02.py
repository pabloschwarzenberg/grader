#Nota final
PT = float(input("ingrese nota de sus tareas:"))
PI = float(input("ingrese nota de interrogaciones:"))
NE = float(input("ingrese nota de su examen:"))
PP = float(input("ingrese nota presentacion:"))
promediofinal = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) +  (0.1 * PP)
promediofinal2 = round(promediofinal,1)
print("El promedio final es:" , promediofinal2)
