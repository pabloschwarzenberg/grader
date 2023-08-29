#Nota final
PT=float(input("Dame la nota de tareas:",))
PI=float(input("Dame la nota de interrogaciones:",))
NE=float(input("Dame la nota de examen:",))
PP=float(input("Dame la nota de presentacion:",))

promedio= (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print("Tu promedio es de:", round(promedio,1))
