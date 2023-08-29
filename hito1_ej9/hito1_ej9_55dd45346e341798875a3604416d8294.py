#Sistema de Ecuaciones
from math import *
argumentos = []
eq_1 = list()
eq_2 = list()
x = 0

for i in range(6):
  num = int(input("Ingrese los argumentos de las ecuaciones:"))
  argumentos.append(num)

for i in range(3):
  mult = argumentos[i] *(-argumentos[3])
  eq_1.append(mult)

for i in range(3,len(argumentos)):
  mult = argumentos[i] *(argumentos[0])
  eq_2.append(mult)

y_1 = [e1 + e2 for e1, e2 in zip(eq_1,eq_2)] # Resultado: [-2, -1, -2, 0, -7, 6, 2]
y_2 = y_1[2] / y_1[1]

if (y_2*argumentos[1]) < 0:
  x = float((argumentos[2] + (argumentos[1]*(y_2*-1)))/argumentos[0])
elif (y_2 * argumentos[1]) >= 0:
  x = float((argumentos[2] - (argumentos[1]*y_2))/argumentos[0])

x = round(x,1)
y = round(y_2,1)

respuesta = ["x={}".format(x),"y={}".format(y)]

print(respuesta)