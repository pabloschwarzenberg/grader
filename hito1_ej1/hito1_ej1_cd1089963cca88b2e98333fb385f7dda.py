#Nota final
PT = float(input("valor tareas:"))
PI = float(input("valor interrogaciones:"))
NE = float(input("valor examenes:"))
PP = float(input("valor presentaciones:"))
promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("el promedio final es",round(promedio,1))