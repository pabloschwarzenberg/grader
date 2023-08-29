#Nota final
variable1="Tareas"
variable2="interrogaciones"
variable3="Examen"
variable4="Presentacion"
PT=float(input("ingrese la nota que obtuvo en tareas: "))
PI=float(input("ingrese las notaas que obtuvo en interrogaciones: "))
NE=float(input("ingrese las notas que obtuvo en Examen: "))
PP=float(input("ingrese las notas que obtuvo en presentacion: "))
calculo=0.3*PT+0.3*PI+0.3*NE+0.1*PP
redondeo=round(calculo,1)
print("Su promedio es",redondeo)