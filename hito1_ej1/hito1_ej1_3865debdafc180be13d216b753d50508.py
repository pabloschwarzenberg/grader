#Nota final
a = eval(input("ingrese nota de tareas :"))         
b = eval(input("ingrese nota de interrogaciones :"))
c = eval(input("ingrese nota de examen :"))
d = eval(input("ingrese nota de presentacion :"))






promedio = ((0.3)*a + (0.3)*b + (0.3)*c + (0.1)*d)
         
promedio_f = round(promedio,1)
print("el pr es: ",str(promedio_f))