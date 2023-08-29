#Nota final
PT = float(input("ingrese nota de tarea: "))
PI = float(input("ingrese nota de interrogaciones : "))
NE = float(input("ingrese nota de examen: "))
PP = float(input("ingrese nota de presentacion: "))


nota1 = 0.3*PT
nota2 = 0.3*PI
nota3 = 0.3*NE
nota4 = 0.1*PP


promedio = (nota1 + nota2 + nota3 + nota4)
redondeado = round(promedio, 1)


print("el promedio es: ",redondeado)