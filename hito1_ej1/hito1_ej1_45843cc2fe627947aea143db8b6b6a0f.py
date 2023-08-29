#Nota final

not1 = eval(input("Ingrese nota de tarea: "))
not2 = eval(input("Ingrese nota de interrogaciones: "))
not3 = eval(input("Ingrese nota de examen: "))
not4 = eval(input("Ingrese nota de presentacion: "))

nota_final = (not1 + 0.3, not2 + 0.3, not3 + 0.3, not4 + 0.1)

nota_final = nota_final // 4

print("El promedio final de su nota es: ",nota_final)