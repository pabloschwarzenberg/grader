#Nota final
pt = float(input("Puntaje tareas: "))
pi = float(input("Puntaje interrogaciones: "))
ne = float(input("Nota exámen: "))
pp = float(input("Puntaje presentaciones: "))
promedioFinal = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

print(round(promedioFinal, 1))