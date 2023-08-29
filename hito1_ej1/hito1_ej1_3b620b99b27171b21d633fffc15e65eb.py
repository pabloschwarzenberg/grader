#Nota final
#Nota final
PT= float(input("Ingrese nota de tarea: "))
PI= float(input ("Ingrese nota de interrogaciones: "))
NE= float(input ("Ingrese nota de examen: "))
PP= float(input ("Ingrese nota de presentación: "))

PTT= 0.3*PT
calculo_1= round (PTT, 1)

PII= 0.3*PI
calculo_2= round (PII, 1)

NEE= 0.3*NE
calculo_3= round (NEE, 1)

PPP= 0.1*PP
calculo_4= round (PPP, 1)

promedio_final= calculo_1 + calculo_2 + calculo_3 + calculo_4
print (promedio_final)
