#Nota final
PT = eval (input("ingresar valor de la nota de  tareas : "))
PI = eval (input("ingresar valor de la nota de interrogaciones: "))
NE = eval (input("ingresar valor de el examen: "))
PP = eval (input("ingresar valor de la presentación: "))
#realizar el calculo
PF = ((PT * 0.3)+(PI * 0.3)+(NE * 0.3)+(PP * 0.1))

#mostrar el resultado


print("el promedio final es: ", round(PF,1) )   