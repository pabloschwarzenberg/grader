#Nota final
#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion 
PT=float(input("ingrese nota de tareas:"))
PI=float(input("ingrese nota de interrogaciones:"))
NE=float(input("ingrese nota de examen:"))
PP=float(input("ingrese nota de presentación:"))
NF=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("su Nota Final es:", NF)