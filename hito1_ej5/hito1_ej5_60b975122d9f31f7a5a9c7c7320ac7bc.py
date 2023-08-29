#Cálculo del dígito verificador de un rut
rut=input()
n=len(rut)
total=0
total=total+2*int(rut[-1])
total=total+3*int(rut[-2])
total=total+4*int(rut[-3])
total=total+5*int(rut[-4])
total=total+6*int(rut[-5])
total=total+7*int(rut[-6])
total=total+2*int(rut[-7])
if n==8:
 total = total+3*int(rut[-8])
resto=total%11
digito=11-resto
if digito==10:
 print('dv=k')
elif digito==11:
 print('dv=0')
else:
 print('dv=', digito)      