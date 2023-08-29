#Cálculo del dígito verificador de un rut
rut= (input('Ingrese su rut '))
rut = rut[::-1]
rut
numeros = sum(c.isdigit() for c in rut)
print("La cantidad de números en la cadena es:", numeros-1)
for i in rut:
  suma=0
  rut1= int(rut[0])
  prm = rut1*2
  rut2= int(rut[1])
  seg = rut2*3
  rut3= int(rut[2])
  trc = rut3*4
  rut4= int(rut[3])
  cua = rut4*5
  rut5= int(rut[4])
  cnc = rut5*6
  rut6= int(rut[5])
  sei = rut6*7
  rut7= int(rut[6])
  sie = rut7*2
  if (numeros-1)>=7:
    rut8= int(rut[7])
    och = rut8*3
    suma = prm+seg+trc+cua+cnc+sei+sie+och
    entero = int(int(suma)/11)
    resto = int(suma)-(11*int(entero))
    final = 11-resto
  else:
    suma = prm+seg+trc+cua+cnc+sei+sie
    entero = int(int(suma)/11)
    resto = int(suma)-(11*int(entero))
    final = 11-resto
print('La suma es ',suma,'\n')
print('El entero es ',entero,'\n')
print('El resto es ',resto,'\n')
print('El resultado final es',final,'\n')
if final == 11:
  print('dv =',0)
elif final == 10:
  print('dv =','K')
else:
  print('dv =', final)