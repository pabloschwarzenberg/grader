#Nota final
tareas=float(input('ingresa nota de tareas:'))

interrogaciones=float(input('ingresa nota interrogaciones:'))

examen=float(input('ingresa nota de examen:'))

presentacion=float(input('ingresa nota de presentacion:'))



sumatoria=float(tareas+interrogaciones+examen+presentacion)
nota_final=float(sumatoria/4)

nota_final=print("nota final:","{:.2f}".format(nota_final))