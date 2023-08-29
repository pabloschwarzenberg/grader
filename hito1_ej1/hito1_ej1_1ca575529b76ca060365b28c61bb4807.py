#Nota final
pt = float(input('Ingrese la nota de sus tareas:'))
pi = float(input('Ingrese la nota de sus interrogaciones:'))
ne = float(input('Ingrese la nota de su examen:'))
pp = float(input('Ingrese la nota de presentacion:'))

ptt = pt*0.3
ppi = pi*0.3
nne = ne*0.3
ppp = pp*0.1

promedio = ptt + ppi + nne + ppp
print(round(promedio,1))