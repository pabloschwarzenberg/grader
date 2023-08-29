#Cálculo del dígito verificador de un rut
rut = str(input("Rut: "))
cantD = list(rut)
cantD1 = len(cantD)
if cantD1 == 8:
  r0 = int(list (rut)[7])
  r1 = int(list (rut)[6])
  r2 = int(list (rut)[5])
  r3 = int(list (rut)[4])
  r4 = int(list (rut)[3])
  r5 = int(list (rut)[2])
  r6 = int(list (rut)[1])
  r7 = int(list (rut)[0])
  rt1 = ((r0*2)+(r1*3)+(r2*4)+(r3*5)+(r4*6)+(r5*7)+(r6*2)+(r7*3))
  rt2 = (round((int(rt1/11)),0))
  rt3 = rt1-(rt2*11)
  rt4 = int(11-rt3)
  if rt4 == 11:
    print ("dv= 0")
  if rt4 == 10:
    print ("dv= K")
  if rt4 > 0 and rt4 < 10:
    print ("dv=",rt4)

if cantD1 == 7:
  r0 = int(list (rut)[6])
  r1 = int(list (rut)[5])
  r2 = int(list (rut)[4])
  r3 = int(list (rut)[3])
  r4 = int(list (rut)[2])
  r5 = int(list (rut)[1])
  r6 = int(list (rut)[0])
  rt1 = ((r0*2)+(r1*3)+(r2*4)+(r3*5)+(r4*6)+(r5*7)+(r6*2))
  rt2 = (round((int(rt1/11)),0))
  rt3 = rt1-(rt2*11)
  rt4 = int(11-rt3)
  if rt4 == 11:
    print ("dv= 0")
  if rt4 == 10:
    print ("dv= K")
  if rt4 > 0 and rt4 < 10:
    print ("dv=",rt4)