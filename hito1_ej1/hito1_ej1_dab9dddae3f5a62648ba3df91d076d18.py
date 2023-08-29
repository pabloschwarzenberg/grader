#Nota final
print("Hola alumno")
nombre = input("Ingrese su nombre: ")
PT = float(input("Ingrese su nota de tareas: "))
PI = float(input("Ingrese su nota de interrogaciones: "))
NE = float(input("Ingrese su nota de examen: "))
PP = float(input("Ingrese su nota de presentacion: "))

n1 = PT*0.30
n2 = PI*0.30
n3 = NE*0.30
n4 = PP*0.10
promedio = n1+n2+n3+n4
prom_red = round(promedio,1)
print(prom_red)
print("Alumno(a)" ,nombre , "su promedio es: " ,promedio ,)     