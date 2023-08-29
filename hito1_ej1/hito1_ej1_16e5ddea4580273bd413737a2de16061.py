x = eval(input("Ingrese la nota de Tareas : "))
y = eval(input("Ingrese la nota de Interrogaciones : "))
w = eval(input("Ingrese la nota de Examen : "))
z = eval(input("Ingrese la nota de Presentacion : "))

nota_final=0.3*x + 0.3*y + 0.3*w + 0.1*z


print("Su nota final es : " ,"{0:.1f}".format(nota_final))