#Entrada
pt = float(input("Nota de tareas: "))
pi = float(input("Nota de interrogaciones: "))
ne = float(input("Nota de examen: "))
pp = float(input("Presentacion: "))

#Procedimiento
if pt < 1:
   print("En pt numeros iguales o mayores a 1")
elif pt > 7:
   print("En pt numeros iguales o menores a 7")
   
if pi < 1:
   print("En pi numeros iguales o mayores a 1")
elif pi > 7:
   print("En pi numeros iguales o menores a 7")
   
if ne < 1:
   print("En ne numeros iguales o mayores 1")
elif ne > 7:
   print("En ne numeros iguales o menores a 7")
   
if pp < 1:
   print("En pp numeros iguales o mayores a 1")
elif pp > 7:
   print("En pp numeros iguales o menores a 7")
   
nf = float(0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp)

#Salida
print("nota final: ", nf)      