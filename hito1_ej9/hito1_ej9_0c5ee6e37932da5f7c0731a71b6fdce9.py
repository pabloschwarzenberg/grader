#Sistema de Ecuaciones
def sistema(a,b,c,d,e,f):
  deter = a * e - b * d
  x = (c * e - b * f) / deter
  y = (a * f - c * d) / deter
  return x,y
ecuacion = []
for i in range (6):
  ecu = eval(input('Ingrese el término'+str(i)+':'))
  ecuacion.append(ecu)
a = ecuacion[0]
b = ecuacion[1]
c = ecuacion[2]
d = ecuacion[3]
e = ecuacion[4]
f = ecuacion[5] 
x,y= sistema(a,b,c,d,e,f)
print('x=',x,'y=',y)