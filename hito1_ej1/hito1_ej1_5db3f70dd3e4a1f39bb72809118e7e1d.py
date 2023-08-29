#Nota final
print("Notas Finales")
Pt= float(input("Ingrese nota de tareas"))
Pi= float(input("Ingrese nota de interrogaciones"))
Ne= float(input("Ingrese nota de examen"))
Pp= float(input("Ingrese nota de presentacion"))

Pf= (Pt*0.3)+(Pi*0.3)+(Ne*0.3)+(Pp*0.1)
print("El resultado final es", round(Pf,1))