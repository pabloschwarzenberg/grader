#Nota final
print("ingrese sus notas")
nota_pt = eval(input("nota tareas: "))
nota_pi = eval(input("nota interrogaciones: "))
nota_ne = eval(input("nota examen: "))
nota_pp = eval(input("nota presetacion: "))

p = round(nota_pt*0.3 + nota_pi*0.3 + nota_ne*0.3 + nota_pp*0.1, 1)
print("Tu promedio es: ", p)       