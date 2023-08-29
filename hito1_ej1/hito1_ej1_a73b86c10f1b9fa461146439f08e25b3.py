#Nota final
      
PT = float(input("Ingrese su nota de tareas: ")) #Tareas
PI = float(input("Ingrese su nota de interrograciones: ")) #Interrogaciones
NE = float(input("Ingrese su nota de examen: ")) #Examen
PP = float(input("Ingrese su nota de presentacion: ")) #Presentacion
#Con ellas calcula el promedio

calculo_promedio = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
promedio = float(calculo_promedio) 
print("Su promedio es: ",promedio,)