#Cálculo del dígito verificador de un rut
rut=(input("Ingrese su rut sin digito verificador:"))
descomposicion=(len(rut)-1)
if(descomposicion==7):
  a=eval(rut[descomposicion])*2
  b=eval(rut[descomposicion-1])*3
  c=eval(rut[descomposicion-2])*4
  d=eval(rut[descomposicion-3])*5
  e=eval(rut[descomposicion-4])*6
  f=eval(rut[descomposicion-5])*7
  g=eval(rut[descomposicion-6])*2
  h=eval(rut[descomposicion-7])*3
  i=(a+b+c+d+e+f+g+h)
  
  division= i//11
  resto= i-(division*11)
  dv=11-resto

  if(dv==10):
    dv="k"
    print("dv=",dv)

  elif(dv==11):
    dv=0
    print("dv=",dv)

  elif(dv!=10 and dv!=11):
    print("dv=",dv)

elif(descomposicion==6):
  a=eval(rut[descomposicion])*2
  b=eval(rut[descomposicion-1])*3
  c=eval(rut[descomposicion-2])*4
  d=eval(rut[descomposicion-3])*5
  e=eval(rut[descomposicion-4])*6
  f=eval(rut[descomposicion-5])*7
  g=eval(rut[descomposicion-6])*2

  i=(a+b+c+d+e+f+g)

  division= i//11
  resto= i-(division*11)
  dv=11-resto

  if(dv==10):
    dv="k"
    print("dv=",dv)

  elif(dv==11):
    dv=0
    print("dv=",dv)

  elif(dv!=10 and dv!=11):
    print("dv=",dv)     