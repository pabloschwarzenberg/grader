#solicitar las 4 notas al usuario 
PT=float(input('ingresar la nota de la tarea(PT): '))
PI=float(input('ingresar la nota de interrogacion(PI): '))
NE=float(input('ingresar la nota de examen(NE): '))
PP=float(input('ingresar la nota de presentacion(PP): '))

#calculo para sacar el promedio final 
promedio_final= 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
#resultado redondeado a decimal 
promedio_final_redondeado=round(promedio_final,1)
print('el promedio final es:', promedio_final_redondeado)
