#Nota final
print("PT = tareas")
print("PI = interrogaciones")
print("NE = examen")
print("PP = presentacion")

PT = float(input("ingrese nota PT: "))
PI = float(input("ingrese nota PI: "))
NE = float(input("ingrese nota NE: "))
PP = float(input("ingrese nota PP: "))

Total = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("su nota final es: ",round(Total,1))   