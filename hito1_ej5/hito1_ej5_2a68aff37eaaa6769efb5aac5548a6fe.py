rut= int(input("Ingresa tu Rut:"))
if 1000000 <= rut <= 9999999:
  
  d7 = rut%10
  rut=rut//10
  
  d6 = rut%10
  rut=rut//10

  d5 = rut%10
  rut=rut//10

  d4 = rut%10
  rut=rut//10

  d3 = rut%10
  rut=rut//10

  d2 = rut%10
  rut=rut//10

  d1 = rut%10
  rut=rut//10
  
  suma= d7*2 + d6*3 + d5*4 + d4*5 + d3*6 + d2*7 + d1*2 

  resto= suma % 11
  resultado= 11 - resto 
  
  if resultado==11:
    print("dv=0")
  else:
    if resultado==10:
      print("dv=K")
    else:
      print("dv=", resultado)
  
else:
  print("Rut invalido")
  
  
  