#Nota final
pt=float(input("promedio tareas:"))
pi=float(input("ingrese promedio interrogaciones:"))
ne=float(input("ingrese nota examen"))
pp=float(input("ingrese nota presentacion:"))

PtPiNeMultiplicador=float(0.3)
ppMultiplicador=float(0.1)
PromedioFinal=PtPiNeMultiplicador*pt+PtPiNeMultiplicador*pi+PtPiNeMultiplicador*ne+ppMultiplicador*pp
print(round(PromedioFinal, 2))