#Nota final
      #Nota final
2
 # Solicitamos las notas al usuario
3
PT = float(input("Ingresa la nota de Tareas: "))
4
PI = float(input("Ingresa la nota de Interrogaciones: "))
5
NE = float(input("Ingresa la nota de Examen: "))
6
PP = float(input("Ingresa la nota de Presentacion: "))
7
 
8
# Calculamos la nota final según la fórmula proporcionada
9
nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
10
 
11
# Imprimimos el resultado redondeado a un decimal
12
print(round(nota_final, 1))