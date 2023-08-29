#Nota final
PT = float(input("Ingrese nota de Tareas PT: "))
PI = float(input("Ingrese nota interrogaciones PI: "))
NE = float(input("Ingrese nota Exámen NE: "))
PP = float(input("Ingrese nota de presentación PP: "))

PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
NF= round(PF,1)
print("Resultado de Nota Final es:", (NF))      