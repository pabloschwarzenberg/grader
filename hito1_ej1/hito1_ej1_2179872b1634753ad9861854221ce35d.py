#Nota final

print("Calculadora de nota final.")

notaT = eval(input("Ingrese su nota por tareas: "))
notaI = eval(input("Ingrese su nota en interrogaciones: "))
notaE = eval(input("Ingrese su nota de exámen: "))
notaP = eval(input("Y finalmente su nota de presentación: "))

promedioF = (0.3 * notaT + 0.3 * notaI + 0.3 * notaE + 0.1 * notaP)
promedioR = round(promedioF, 2)
print(promedioR)