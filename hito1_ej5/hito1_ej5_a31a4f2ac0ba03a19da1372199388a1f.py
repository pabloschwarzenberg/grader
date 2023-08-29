#Cálculo del dígito verificador de un rut

rut=input()

if (len(rut))==8:

  uno=int(rut[0])
  dos=int(rut[1])
  tres=int(rut[2])
  cuatro=int(rut[3])
  cinco=int(rut[4])
  seis=int(rut[5])
  siete=int(rut[6])
  ocho=int(rut[7])

  a=ocho*2
  b=siete*3
  c=seis*4
  d=cinco*5
  e=cuatro*6
  f=tres*7
  g=dos*2
  h=uno*3

  suma=a+b+c+d+e+f+g+h
  
  resto=suma%11

  final=11-resto

  if final==11:
    print("dv=0")
  elif final==10:
    print("dv=K")
  else:
    print("dv=",final)

else:
  uno=int(rut[0])
  dos=int(rut[1])
  tres=int(rut[2])
  cuatro=int(rut[3])
  cinco=int(rut[4])
  seis=int(rut[5])
  siete=int(rut[6])
  
  a=siete*2
  b=seis*3
  c=cinco*4
  d=cuatro*5
  e=tres*6
  f=dos*7
  g=uno*2


  suma=a+b+c+d+e+f+g

  resto=suma%11

  final=11-resto

  if final==11:
    print("dv=0")
  elif final==10:
    print("dv=K")
  else:
    print("dv=",final)