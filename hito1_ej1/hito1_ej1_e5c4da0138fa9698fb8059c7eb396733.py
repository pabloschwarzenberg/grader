#Nota final

PT=float(input("ingrese notas de Tarea:"))
PI= float(input("ingrese notas de Interrogaciones:"))
NE= float(input("ingrese notas de Examenes:"))
PP= float(input("ingrese notas de Presentacion:"))

promedio_final=float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("el resultado redondeado es:",round(promedio_final,1) )