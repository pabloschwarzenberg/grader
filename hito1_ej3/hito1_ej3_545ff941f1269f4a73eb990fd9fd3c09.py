#Aprobación de créditos
i=int(input())
an=int(input())
nh=int(input())
ab=int(input())
ec=input()
uor=input()
#1Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if ab>10 and nh>=2:
  print('APROBADO')
#2Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif ec=="C" and nh>3 and 45<=2017-an<=55:
  print('APROBADO')
#3Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif i>2500000 and ec=="S" and U:
  print('APROBADO')
#4Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif i>3500000 and ab>5:
  print('APROBADO')
#5Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif uor=="R" and ec=='C' and nh<2:
  print('APROBADO')
else:
  print('RECHAZADO')