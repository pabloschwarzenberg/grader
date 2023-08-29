#Cálculo del dígito verificador de un rut
rut=input('Ingrese rut sin digito ')
rut=str(rut)
if len(rut)== 8:
  v1=int(rut[0])
  v2=int(rut[1])
  v3=int(rut[2])
  v4=int(rut[3])
  v5=int(rut[4])
  v6=int(rut[5])
  v7=int(rut[6])
  v8=int(rut[7])
  formula= v8*2+v7*3+v6*4+v5*5+v4*6+v3*7+v2*2+v1*3
  formula2=int(formula/11)
  formula3=int(formula-(11*formula2))
  formula4=int(11-formula3)
  if formula4==10 or formula4==11:
    if formula4==11:
      print("dv=0")
    elif formula4==10:
      print("dv=K")
  else:
    print("dv=",formula4)
  
else:
  v1=int(rut[0])
  v2=int(rut[1])
  v3=int(rut[2])
  v4=int(rut[3])
  v5=int(rut[4])
  v6=int(rut[5])
  v7=int(rut[6])
  formula= v7*2+v6*3+v5*4+v4*5+v3*6+v2*7+v1*2
  formula2=int(formula/11)
  formula3=int(formula-(11*formula2))
  formula4=int(11-formula3)
  if formula4==10 or formula4==11:
    if formula4==11:
      print("dv=0")
    elif formula4==10:
      print("dv=K")
  else:
    print("dv=",formula4)
  
 