rut=int(input('Ingresa tu rut sin digito verificador: '))
RUT=list(str(rut))
rdig8=int(RUT[7])*2
rdig7=int(RUT[6])*3
rdig6=int(RUT[5])*4
rdig5=int(RUT[4])*5
rdig4=int(RUT[3])*6
rdig3=int(RUT[2])*7
rdig2=int(RUT[1])*2
rdig1=int(RUT[0])*3
suma=rdig1+rdig2+rdig3+rdig4+rdig5+rdig6+rdig7+rdig8
if 11-(suma%11) == 11:
  dv=0
elif 11-(suma%11) == 10:
  dv='K'
else:
  dv=11-(suma%11)
print('dv=', end='')
print(dv)