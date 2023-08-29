#Nota final
PT=float(input("ingrese las notas de su tarea:"))  
PI=float(input("ingrese sus nota de interrogacion:"))
NE=float(input("ingrese nota examen:"))
PP=float(input("ingrese nota de presentacion:"))
P=(0,3*PT)+(0,3*PI)+(0,3*NE)+(0,1*PP)
round(P,2)
print("su nota final es:",P)