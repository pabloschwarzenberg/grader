#Nota final
PT=float(input("Ingresa nota de tareas:"))
PI=float(input("Ingresa nota de interrogaciones:"))
NE=float(input("Ingresa nota de examen:"))
PP=float(input("Ingresa nota de presentacion:"))

promedioFinal=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
a=round(promedioFinal,1)
print(a)
      