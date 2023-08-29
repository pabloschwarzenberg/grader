#Nota final
#Ingrese valor
PT= float(input("Nota de tareas que tuvo:\n"))
PI= float(input("Nota de interrogaciones que tuvo:\n"))
NE= float(input("Nota de examenes que tuvo:\n"))
PP= float(input("Nota de presentaciones que tuvo:\n"))
#Formula de calculo del promedio
Promedio_final= (0.3 * PT+ 0.3 * PI + 0.3 * NE + 0.1 * PP)
#Imprimir promedio final en pantalla
print("Su promedio es de final :" ,round(Promedio_final,1))