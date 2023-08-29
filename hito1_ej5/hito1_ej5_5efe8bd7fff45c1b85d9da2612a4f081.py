#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese el rut sin el digito verificador: \n "))

rt = str(rut)

len(rt)

if len(rt) == 8:
  v1 = float(rt[0])
  v2 = float(rt[1])
  v3 = float(rt[2])
  v4 = float(rt[3])
  v5 = float(rt[4])
  v6 = float(rt[5])
  v7 = float(rt[6])
  v8 = float(rt[7])
  
  div1 = ((v8*2)+(v7*3)+(v6*4)+(v5*5)+(v4*6)+(v3*7)+(v2*2)+(v1*3))

  total1 = (div1/11)

  total2 =div1-(11*int(total1))

  total3 = (11-total2)


elif len(rt) == 7:
  vv1 = float(rt[0])
  vv2 = float(rt[1])
  vv3 = float(rt[2])
  vv4 = float(rt[3])
  vv5 = float(rt[4])
  vv6 = float(rt[5])
  vv7 = float(rt[6])

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