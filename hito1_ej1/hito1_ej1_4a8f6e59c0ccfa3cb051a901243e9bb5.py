#Nota final
pt = eval(input("ingrese su nota en tareas:"))
pi = eval(input("ingrese su nota en interrogaciones:"))
ne = eval(input("ingrese su nota en examen:"))
pp = eval(input("ingrese su nota en presentacion:"))

#0.3PT + 0.3PI + 0.3NE + 0.1PP

nota1 = pt * 0.3
nota2 = pi * 0.3
nota3 = ne * 0.3
nota4 = pp * 0.1

promedio = nota1 + nota2 + nota3 + nota4

print("su promedio de notas es:",promedio)      