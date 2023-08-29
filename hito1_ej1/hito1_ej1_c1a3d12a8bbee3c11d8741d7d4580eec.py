PT = float(input("Ingresa tu nota de Tareas: "))
PI = float(input("Ingresa tu nota de Interrogaciones: "))
NE = float(input("Ingresa tu nota del Examen: "))
PP = float(input("Ingresa tu nota de la Presentacion: "))
PTP = 0.3*PT
PIP = 0.3*PI
NEP = 0.3*NE
PPP=  0.1*PP
promedio = PTP+PIP+NEP+PPP
print(round(promedio,1))