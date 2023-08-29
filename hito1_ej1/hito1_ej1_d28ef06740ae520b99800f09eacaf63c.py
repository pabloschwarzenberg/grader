def prom(a, b, c, d):
  final = (0.3*a + 0.3*b + 0.3*c + 0.1*d)
  return final
PT= float(input("Ingrese nota de TAREAS:"))
PI= float(input("Ingrese nota de INTERROGACIONES: \n"))
NE= float(input("Ingrese nota de EXAMEN: \n"))
PP= float(input("Ingrese nota de PRESENTACION: \n"))

print (prom(PT, PI, NE, PP))