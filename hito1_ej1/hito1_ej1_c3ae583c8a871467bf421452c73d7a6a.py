x = float(input("ingrese la nota de tareas: "))

y = float(input("ingrese la nota de Interrogaciones :"))
z = float(input("ingrese la nota de Examen :"))
a = float(input("ingrese la nota de Presentacion :"))
nota= x*0.3+y*0.3+z*0.3+a*0.1
nota_final=round(nota,1)
print("su promedio final es",nota_final)
