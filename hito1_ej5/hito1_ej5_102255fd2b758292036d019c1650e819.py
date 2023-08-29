#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese el rut sin el digito verificador: "))

rut2 = str(rut)

len(rut2)

if len(rut2) == 8:
  v1 = float(rut2[0])
  v2 = float(rut2[1])
  v3 = float(rut2[2])
  v4 = float(rut2[3])
  v5 = float(rut2[4])
  v6 = float(rut2[5])
  v7 = float(rut2[6])
  v8 = float(rut2[7])
  
  div1 = ((v8*2)+(v7*3)+(v6*4)+(v5*5)+(v4*6)+(v3*7)+(v2*2)+(v1*3))

  total1 = (div1/11)

  total2 =div1-(11*int(total1))

  total3 = (11-total2)


elif len(rut2) == 7:
  vv1 = float(rut2[0])
  vv2 = float(rut2[1])
  vv3 = float(rut2[2])
  vv4 = float(rut2[3])
  vv5 = float(rut2[4])
  vv6 = float(rut2[5])
  vv7 = float(rut2[6])

  div2 = ((vv7*2)+(vv6*3)+(vv5*4)+(vv4*5)+(vv3*6)+(vv2*7)+(vv1*2))

  total1 = (div2/11)

  total2 =div2-(11*int(total1))

  total3 = (11-total2)
  



if total3 == 11:
  print ("dv= 0")

elif total3 == 10:
  print ("dv= K")

else:
  print (("dv= "), int(total3))