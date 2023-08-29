PT = float(input('nota tareas: '))
PI = float(input('nota interrogaciones: '))
PE = float(input('nota examen: '))
PP = float(input('nota presentacion: '))
PT *= 0.3
PI *= 0.3
PE *= 0.3
PP *= 0.1
NF = round((PT+PI+PE+PP),1)
print(NF)
      