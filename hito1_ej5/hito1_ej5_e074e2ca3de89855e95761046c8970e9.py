rut = str(input('Ingrese su rut para cacular su dígito verificador: '))


if int(rut) < 10000000:
  resultado = int(rut[-1])*2 + int(rut[-2])*3 + int(rut[-3])*4 + int(rut[-4])*5 + int(rut[-5])*6 + int(rut[-6])*7 + int(rut[-7])*2

elif int(rut) < 100000000:
  resultado = int(rut[-1])*2 + int(rut[-2])*3 + int(rut[-3])*4 + int(rut[-4])*5 + int(rut[-5])*6 + int(rut[-6])*7 + int(rut[-7])*2 + int(rut[-8])*3

resultado2 = resultado//11
total = resultado - (11*resultado2)
total = 11-total

if total == 11:
  total = 0
elif total == 10:
  total = 'K'



print('dv=',total)
