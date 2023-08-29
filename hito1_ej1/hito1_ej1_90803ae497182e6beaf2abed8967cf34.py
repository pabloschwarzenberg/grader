#Entrada
PT=float(input("ingrese las notas de las tareas: "))
PI=float(input("ingrese las notas de las interrogaciones: "))
NE=float(input("ingrese las notas de los examenes: "))
PP=float(input("ingrese las notas de las presentaciones: "))
 
#Formula
promediofinal= (0.3*PT+0.3*PI+0.3*NE+0.1*PP)

#Salida
print("el promedio final es:", promediofinal)