#Nota final
PT = float(input("ingrese las notas de las tareas:"))
PI = float(input("ingrese las notas de las interrogaciones:"))
NE = float(input("ingrese las notas de los Examenes:"))
PP = float(input("ingrese las notas de las Presentaciones:"))
A = (PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1)
B = round(A,1)
print(B)
