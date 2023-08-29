#Nota final
pTareas=float(input("Introduzca nota de tareas:"))
pInterrogaciones=float(input("Introduzca nota de interrogaciones:"))
nExamen=float(input("Introduzca nota de examen:"))
pPresentacion=float(input("Introduzca nota de presentacion:"))
notaFinal=(0.3*pTareas)+(0.3*pInterrogaciones)+(0.3*nExamen)+(0.1*pPresentacion)
print("Su nota final es","{:.2}".format(notaFinal))