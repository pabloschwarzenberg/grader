#Nota final
PT = float(input("Tu nota de tareas: "))
PI = float(input("Tu nota de interrogaciones: ")) 
NE = float(input("Tu nota de examen: ")) 
PP = float(input("Tu nota de presentacion: "))
PF = PT * 0.3 + PI * 0.3 + NE * 0.3 + PP * 0.1
PF2 = round(PF,1)
print(PF2)