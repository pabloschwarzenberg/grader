#Nota final

#entranda

PT = float(input("ingrese su nota de tareas >>>"))
PI = float(input("ingrese su nota de interrogaciones >>>"))
NE = float(input("ingrese la nota final del examen >>>"))
PP = float(input("ingrese se nota de presentacion >>>"))

#procesamiento

nota_final = (0.3*PT) +  (0.3*PI) + (0.3*NE) + (0.1*PP)
nota_final = float (round(nota_final, 1))

#salida

print ("su nota es" , nota_final)   