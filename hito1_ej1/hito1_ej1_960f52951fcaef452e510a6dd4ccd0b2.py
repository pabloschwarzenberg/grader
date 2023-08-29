#Nota final
T = eval(input("ingrese notas por tareas"))
I = eval(input("ingrese notas por interrogaciones"))
E= eval(input("ingrese notas por examenes"))
P = eval(input("ingrese notas por precentaciones"))
p = round(0.3*T + 0.3*I + 0.3*E + 0.1*P , 1)
print("promedio igual a:",p)
