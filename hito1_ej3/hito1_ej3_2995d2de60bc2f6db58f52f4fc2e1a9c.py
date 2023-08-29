#Aprobación de créditos
S= 'casado'
C= 'soltero'
U= 'urbano'
R= 'rural'
i=int(input("ingresos: "))
an=int(input("año de nacimiento: "))
nh=int(input("numero de hijos: "))
ab=int(input('años de pertenencia al banco:'))
ec=input('estado civil c o s:')
v=input("vive en zona rural R o urbano U:")
edad= (2021-an)
if ab>10 and nh>=2 and i>0: 
 print('APROVADO')
elif ec== C and 45<edad>55 and nh>=3 and i>0 and ab>0 and v==R or v==U:
  print('APROVADO')
elif i>2500000 and ec==S and v==U and nh>=0 and edad>= 0 and ab>=0:
 print('APROVADO')
elif i>3500000 and ab>5 and ec==C or ec==S and v==R or v==U and nh>=0:
 print('APROVADO')
elif v==R and ec==C and nh<2 and i>=0 and ab>=0 and an>=0:
 print('APROVADO')
else:
 print('rechazado')