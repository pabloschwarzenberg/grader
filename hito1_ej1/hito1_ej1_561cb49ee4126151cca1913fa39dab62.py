#Nota final
      print("ingrese la nota de las tareas:")
PT = float(input())
print("ingrese nota de interogaciones:")
PI = float(input())
print("ingrese nota de examen:")
NE = float(input())
print("ingrese nota de presentacion:")
PP = float(input())

promedio =(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print(" el promedio final es:",round(promedio,1))
