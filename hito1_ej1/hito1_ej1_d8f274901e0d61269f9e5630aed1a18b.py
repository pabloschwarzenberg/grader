#Nota final

#Promedios de los cursos
Pt = float(input("Digite nota Tareas: "))
Pi = float(input("Digite nota Interrogaciones: "))
Ne = float(input("Digite nota Examen: "))
Pp = float(input("Digite nota Presentaciones : ")) 

#Formula
promedio = (0.3*Pt+0.3*Pi+0.3*Ne+0.1*Pp)

#Promedio final
print("El promedio final del curso es: ", round(promedio,1))