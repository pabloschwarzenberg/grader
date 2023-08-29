#Nota final
#Entrada
PT= float(input("Ingrese nota PT: "))  #PT= Tareas
PI= float(input("Ingrese nota PI: "))  #PI= Interrogaciones
NE= float(input("Ingrese nota NE: "))  #NE= Examen
PP= float(input("Ingrese nota PP: "))  #PP= Presentaciones

#Procesamiento

Nota_Final= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

#Salida

print("Estimadx su nota final es", round(Nota_Final,1))