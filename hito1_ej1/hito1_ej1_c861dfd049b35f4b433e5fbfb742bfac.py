#Nota final
print("Ingresar por favor las cuatro notas solicitadas")

pt = eval(input("Nota de Tareas: "))
pi = eval(input("Nota de Interrogaciones: "))
ne = eval(input("Nota de Examen: "))
pp = eval(input("Nota de Presentacion: "))

n1=0.3*pt
n2=0.3*pi
n3=0.3*ne
n4=0.1*pp

promedio = n1+n2+n3+n4
print("El resultado del promedio es: ","{:.1f}".format(promedio))      