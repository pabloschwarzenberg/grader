# inicio
pt = float(input("Ingrese nota de tareas >>"))
pi = float(input("ingrese nota de interrogaciones >>"))
ne = float(input("ingrese nota de examen >>"))
pp = float(input("ingrese nota de presentacion >>"))
#desarrollo
nota1 = float(pt*0.3)
nota2 = float(pi*0.3)
nota3 = float(ne*0.3)
nota4 = float(pp*0.1)
promedio = (nota1 + nota2 + nota3 + nota4)
print(format(promedio,'0.1f'))