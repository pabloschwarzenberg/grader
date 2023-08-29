#Cálculo del dígito verificador de un rut
rut=int(input('ingrese su rut sin puntos ni digito verificador:'))
d1=(rut%10)
rut=rut//10
d2=(rut%10)
rut=rut//10
d3=(rut%10)
rut=rut//10
d4=(rut%10)
rut=rut//10
d5=(rut%10)
rut=rut//10
d6=(rut%10)
rut=rut//10
d7=(rut%10)
rut=rut//10
d8=(rut%10)

suma=(d1*2 + d2*3 + d3*4 + d4*5 + d5*6 + d6*7 + d7*2 + d8*3)%11
dv= 11-suma

if dv == 10:
  print('dv=k')
elif dv == 11:
  print('dv=0')
else:
  print('dv=',dv)