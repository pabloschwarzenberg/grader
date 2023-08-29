#Nota final
print("Programa para calcular nota")
#PT = notas tareas
PT= float(input("Ingrese la nota correspondiente a tareas: "))
#Pi = notas interrigaciones
Pi = float(input("Ingrese la nota correspondiente a interrogaciones: "))
#NE = nota examen
NE = float(input("Ingrese la nota correspondiente al examen: "))
#PP = nota presentacion
PP = float(input("Ingrese la nota de presentacion: "))

calculo_promedio = ((PT) * 0.3 + (Pi) * 0.3 + (NE) * 0.3 + (PP) * 0.1)
print(round(calculo_promedio,1))
      