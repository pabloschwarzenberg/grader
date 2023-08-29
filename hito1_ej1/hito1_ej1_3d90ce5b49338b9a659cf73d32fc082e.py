#Nota final
PTarea = float(input("Ingrese nota de Tareas: "))
PInte = float(input("Ingrese nota de Interrogaciones: "))
NExam = float(input("Ingrese nota de Examenes: "))
PPres = float(input("Ingrese nota de Presentaciones: "))
notaFinal = ((0.3)*PTarea) + ((0.3)*PInte) + ((0.3)*NExam) + ((0.1)*PPres)
print("La nota final corresponde a:", "{0:.1f}".format(notaFinal))      