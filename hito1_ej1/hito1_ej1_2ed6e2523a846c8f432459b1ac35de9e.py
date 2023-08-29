#Nota final
PT = float(input("Ingrese Tareas: "))
PI = float(input("Ingrese Interrogantes: "))
NE = float(input("Ingrese Examen: "))
PP = float(input("Ingrese Presentacion: "))
NPE = ((PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1))
print ("Nota Final : ", round(NPE,1)) 