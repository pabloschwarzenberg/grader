#PromedioFranciscoFernandez
pt=float(input("ingresa la nota de tarea: "))
pi=float(input("ingresa la nota de interrogacion: "))
ne=float(input("ingresa la nota de examen: "))
pp=float(input("ingresa la nota de presentación: "))

pr=round((pt*0.3)+(pi*0.3)+(ne*0.3)+(pp*0.1),1)
print("su nota final es: ",pr)