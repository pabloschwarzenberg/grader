#Nota final
PT=float(input("ingrese nota tareas"))
PI=float(input("ingrese nota de interrogaciones"))
NE=float(input("ingrese nota examen"))
PP=float(input("ingrese nota presentacion"))
PF=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
PF=round(PF,1)
print("el promedio final es",PF)
  