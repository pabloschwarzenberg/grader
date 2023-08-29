#Nota final
pt = eval(input("tareas"))
pi = eval(input("interrogaciones"))
Ne = eval(input("examen"))
pp = eval(input("presentacion"))

Nota_final = (pt*0.3 + pi*0.3 + Ne*0.3 + pp*0.1)

print("su nota final es", round(Nota_final,1))     