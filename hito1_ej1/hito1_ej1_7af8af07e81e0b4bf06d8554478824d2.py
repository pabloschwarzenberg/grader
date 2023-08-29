#Fabian
PT=float(input("Escriba la nota que obtuvo en sus tareas "))
PI=float(input("Escriba la nota que obtuvo en sus interrogaciones "))
NE=float(input("Escriba la nota que obtuvo en sus examen "))
PP=float(input("Escriba la nota que obtuvo en sus presentaciones "))
promedio=(0.3*PI)+(0.3*PT)+(0.3*NE)+(0.1*PP)
print(round(promedio,1))