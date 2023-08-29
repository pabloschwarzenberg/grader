PT = eval(input("Ingresa tu promedio de tareas -> "))

PI = eval(input("Ingresa tu promedio de interrogaciones -> "))

NE = eval(input("Ingresa tu nota de exámen -> "))

PP = eval(input("Ingresa tu promedio de presentación -> "))

promedioFinal = ((PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1))
print(round(promedioFinal, 1))