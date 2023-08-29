#Nota final
PT = float(input("Tu nota de tarea sera: "))
PI = float(input("Tu nota de interrogaciones sera: "))
NE = float(input("Tu nota de examen sera: "))
PP = float(input("Tu nota de presentacion sera: "))
PF = PT * 0.3 + PI * 0.3 + NE * 0.3 + PP * 0.1
PF1 = round(PF , 1)
print(PF1)
