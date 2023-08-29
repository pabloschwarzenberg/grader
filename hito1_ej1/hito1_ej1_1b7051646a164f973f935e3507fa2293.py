#NOTA FINAL

#ENTRADA
pt = float(input('Ingrese la nota de Tareas: '))
pi = float(input('Ingrese la nota de Interrogaciones: '))
ne = float(input('Ingrese la nota de Examen: '))
pp = float(input('Ingrese la nota de Presentacion: '))

#PROCESAMIENTO

nota = (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

#SALIDA
print(round(nota,1))
      