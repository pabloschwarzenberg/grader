#Nota final
PT= eval(input("ingrese su nota de tareas: "))
PI= eval(input("ingrese su nota de interrogaciones: "))
NE= eval(input("ingrese su nota de examen: "))
PP= eval(input("ingrese su nota de presentacion: "))
Notas= PT+ PI +NE
NotaFinal= (Notas*0.3)+(PP*0.1)
print(round(NotaFinal, 1))
