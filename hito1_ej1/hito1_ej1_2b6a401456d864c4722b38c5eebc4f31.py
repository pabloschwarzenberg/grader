#Nota final
 #ENTRADA
#Ingrese numero para PT Tareas
PT = float(input("Ingrese un numero: "))
#Ingrese numero para PI Interrogaciones
PI= float(input("Ingrese un numero: "))
#Ingrese numero para NE Examen
NE = float(input("Ingrese un numero: ")) 
#Ingrese numero para PP Presentacion
PP = float(input("Ingrese un numero: "))
                
#PROCESAMIENTO
nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
                      
#SALIDA
print("La nota final del curso es: ", round(nota_final,1))     