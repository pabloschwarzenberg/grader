#Nota final
PT = eval(input("ingrese notas de su tarea:" ))
PI = eval(input("ingrese notas de la interrogacion:" ))
NE = eval(input("ingrese notas del examen:" ))
PP = eval(input("ingrese notas de su presentacion:" ))
suma = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

promedio = suma/1

x = round(promedio,1)

print("%1.1f" % x )