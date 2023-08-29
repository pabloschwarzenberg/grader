#Nota final
#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion


pt=eval(input("Ingrese nota de tareas:"))
pi=eval(input("Ingrese nota de Interragociones:"))
ne=eval(input("Ingrese nota de Examenes:"))
pp=eval(input("Ingrese nota de Presentaciones:"))

promedioFinal=(0.3*pt) + (0.3*pi)+ (0.3*ne) + (0.1*pp)
print(round(promedioFinal,1))

      