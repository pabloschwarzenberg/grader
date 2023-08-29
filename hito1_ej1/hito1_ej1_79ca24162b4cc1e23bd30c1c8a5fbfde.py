import math
import random
nota_tareas=float(input())
a=nota_tareas
nota_interrogaciones=float(input())
b=nota_interrogaciones
nota_examen=float(input())
c=nota_examen
nota_presentacion=float(input())
d=nota_presentacion
if 1<=a<=7 and 1<=b<=7 and 1<=c<=7 and 1<=d<=7:
  print(round((a*0.3+b*0.3+c*0.3+d*0.1),1))