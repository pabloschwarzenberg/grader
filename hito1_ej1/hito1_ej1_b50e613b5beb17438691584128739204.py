#Nota final
notapt=float(input("Ingrese nota de tareas:"))
notapi=float(input("Ingrese nota promedio de interrogaciones:"))
notane=float(input("Ingrese nota del examen:"))
notap=float(input("Ingrese nota de presentación:"))


calculonotaf=float(0.3*notapt+0.3*notapi+notane*0.3+notap*0.1)
print(round(calculonotaf,1))
