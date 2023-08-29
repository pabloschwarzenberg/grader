#Nota final
print("un usuario tuvo las siguientes notas")
PT = eval(input("ingrese su notas por tareas:"))
PI = eval(input("Ingrese su notas por interrogaciones:"))
NE = eval(input("Ingrese su nota de examen:"))
PP = eval(input("ingrese su nota de presentacion:"))
notafinal = 0.3*PT + 0.3*PI + 0.1*PP + 0.3*NE
notafinalv2 = round(notafinal,1)
print("su promedio final fue de:",notafinalv2)      