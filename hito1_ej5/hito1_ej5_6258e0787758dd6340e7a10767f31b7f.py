rut = str(input(" Ingrese el Rut: "))
cantidadP = list(rut)
cantidadP1 = len(cantidadP)
if cantidadP1 == 8:
  x0 = int(list (rut)[7])
  x1 = int(list (rut)[6])
  x2 = int(list (rut)[5])
  x3 = int(list (rut)[4])
  x4 = int(list (rut)[3])
  x5 = int(list (rut)[2])
  x6 = int(list (rut)[1])
  x7 = int(list (rut)[0])
  rt1 = ((x0*2)+(x1*3)+(x2*4)+(x3*5)+(x4*6)+(x5*7)+(x6*2)+(x7*3))
  rt2 = (round((int(rt1/11)),0))
  rt3 = rt1-(rt2*11)
  rt4 = int(11-rt3)
  if rt4 == 11:
    print ("dv= 0")
  if rt4 == 10:
    print ("dv= K")
  if rt4 > 0 and rt4 < 10:
    print ("dv=",rt4)

if cantidadP1 == 7:
  x0 = int(list (rut)[6])
  x1 = int(list (rut)[5])
  x2 = int(list (rut)[4])
  x3 = int(list (rut)[3])
  x4 = int(list (rut)[2])
  x5 = int(list (rut)[1])
  x6 = int(list (rut)[0])
  rt1 = ((x0*2)+(x1*3)+(x2*4)+(x3*5)+(x4*6)+(x5*7)+(x6*2))
  rt2 = (round((int(rt1/11)),0))
  rt3 = rt1-(rt2*11)
  rt4 = int(11-rt3)
  if rt4 == 11:
    print ("dv= 0")
  if rt4 == 10:
    print ("dv= K")
  if rt4 > 0 and rt4 < 10:
    print ("dv=",rt4)