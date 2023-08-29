#Nota final
PT= float(input("Ingrese la nota de las tareas "))
PI= float(input("Ingrese la nota de las interrogaciones "))
NE= float(input("Ingrese la nota de los examenes "))
PP= float(input("Ingrese la nota de las presentaciones "))
n1= 0.3*PT
n2= 0.3*PI
n3= 0.3*NE
n4= 0.1*PP
notafinal= round(n1+n2+n3+n4,1)
print("El promedio final es ",notafinal)      