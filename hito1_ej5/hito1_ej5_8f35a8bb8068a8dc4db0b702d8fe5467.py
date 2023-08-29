rut = input("ingrese su numero de identificación: ")

if int(rut)>10000000:
    
  a = int(rut[7:])
  b = int(rut[6:7])
  c = int(rut[5:6])
  d = int(rut[4:5])
  e = int(rut[3:4])
  f = int(rut[2:3])
  g = int(rut[1:2])
  h = int(rut[:1])

  suma = a*9 + b*8 + c*7 + d*6 + e*5 + f*4 + g*9 + h*8
  res = suma%11

  if res !=10:
      print("dv= ",res)

  else:
      print("dv = k")

elif int(rut)<10000000:

  a = int(rut[6:])
  b = int(rut[5:6])
  c = int(rut[4:5])
  d = int(rut[3:4])
  e = int(rut[2:3])
  f = int(rut[1:2])
  g = int(rut[:1])

  suma = a*9 + b*8 + c*7 + d*6 + e*5 + f*4 + g*9
  res = suma%11

  if res !=10:
      print("dv= ",res)

  else:
      print("dv = k")