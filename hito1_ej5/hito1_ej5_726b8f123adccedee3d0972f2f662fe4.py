#Cálculo del dígito verificador de un rut
print("Calculadora numero verificador del rut")
rut = int(input("Porfavor escriba el numero del rut sin puntos: "))

rut2 = str(rut)

if rut <= 99999999 and rut >= 9999999:
  pri = rut2[7:8]
  pri = int(pri)
  seg = rut2[6:7]
  seg = int(seg)
  ter = rut2[5:6]
  ter = int(ter)
  cur = rut2[4:5]
  cur = int(cur)
  quin = rut2[3:4]
  quin = int(quin)
  sext = rut2 [2:3]
  sext = int (sext)
  sept = rut2 [1:2]
  sept = int(sept)
  oct = rut2 [0:1]
  oct = int(oct)

  pri = pri * 2
  seg = seg * 3
  ter = ter * 4
  cur = cur * 5
  quin = quin * 6
  sext = sext * 7
  sept = sept * 2
  oct = oct * 3

  cal = (pri + seg + ter + cur + quin + sext +sept + oct) % 11
  det = 11 - cal
  if det == 11:
    print("dv=0")
  elif det == 10:
    print("dv=k")
  else:
    print("dv=", det)

elif rut <= 9999999 and rut > 999999:
  pri = rut2[6:7]
  pri = int(pri)
  seg = rut2[5:6]
  seg = int(seg)
  ter = rut2[4:5]
  ter = int(ter)
  cur = rut2[3:4]
  cur = int(cur)
  quin = rut2 [2:3]
  quin = int (quin)
  sext = rut2 [1:2]
  sext = int(sext)
  sept = rut2 [0:1]
  sept = int(sept)

  pri = pri * 2
  seg = seg * 3
  ter = ter * 4
  cur = cur * 5
  quin = quin * 6
  sext = sext * 7
  sept = sept * 2
  

  cal = (pri + seg + ter + cur + quin + sext +sept) % 11
  det = 11 - cal
  if det == 11:
    print("dv=0")
  elif det == 10:
    print("dv=k")
  else:
    print("dv=", det)
else:
  print("El numero introducido es invalido")

  
      