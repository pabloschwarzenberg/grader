#Nota final
pt = float(input("ingrea tus notas de tareas "))
pi = float(input("ingrea tus notas de interrogaciones "))
ne = float(input("ingrea tus notas de examen "))
pp = float(input("ingrea tus notas de presentacion "))

pf = float(0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp)
print("tu nota es : ", pf)
