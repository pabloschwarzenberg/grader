#Nota final
PT = float(input("ingrese la nota de tareas"))
PI = float(input("ingree la nota de interogaciones"))
NE = float(input("ingree la nota del examen"))
PP = float(input("la nota de presentacion"))
promediofinal = 0.3*PT + 0.3*PI + NE*0.3 + 0.1*PP
pf = round(promediofinal, 1)
print("el promedio final es",pf)
      