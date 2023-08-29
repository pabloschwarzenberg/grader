#Entrada

PT = float(input("Ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de la presentación: "))

#Procesamieto y salida

promedio = (PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1)

 

if(PT>7)or(PT>7)or(NE>7)or(PP>7):
   
    print("Notas no validas")

else:
    print("El promedio final es: ", round(promedio,1))

