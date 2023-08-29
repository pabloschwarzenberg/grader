#Nota final
#Pedimos ingresar las notas 
PT = float(input("Ingrese las notas de tareas: "))
PI = float(input("Ingrese las notas de Interrogaciones: "))
NE = float(input("Ingrese las notas de Examen: "))
PP = float(input("Ingrese las notas de Presentacion: "))

#Vemos el calculo utilizando las variables
Calculo_final = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

# Redondear el promedio final a un decimal
Calculo_final = round(Calculo_final, 1)


#Finalmente, imprimimos el resultado
print("El resultado final es: ",Calculo_final)


      