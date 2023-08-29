i=eval(input('Ingresos: '))
an=eval(input('Año nacimiento: '))
nh=eval(input('Numero hijos: '))
ap=eval(input('Años de pertenencia al banco: '))
ec=input("Soltero o Casado (S/C): ")
svcc=input('Ciudad o Campo (U/R): ')
a=(2020-an)
if (10<=ap) and nh>=2:
  print("APROBADO")
elif ec=='C' and 3>=nh and (a>=45 and a<=55):
  print("APROBADO")
elif i>=2500000 and ec=='S' and svcc=='U':
  print("APROBADO")
elif i>=3500000 and ap>=5:
  print("APROBADO")
elif svcc=='R' and ec=='C' and nh<2:
  print("APROBADO")
else:
  print("RECHAZADO")