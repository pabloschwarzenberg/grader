print('bienvenido al banco UFT, si desea solicitar una aprobación de crédito debe llenar el siguiente formulario, una vez llenado el formulario se evaluará si califica para el crédito')
i=int(input('ingrese su ingreso en pesos sin puntos: '))
na=int(input('ingrese el año de su nacimiento: '))
hi=int(input('ingrese la cantidad de hijos que tiene: '))
cli=int(input('ingrese la cantidad de años que lleva siendo cliente del banco: '))
civ=input('ingrese su estado civil (S: soltero, C: casado): ')
hog=input('ingrese si vive en campo o ciudad (U: urbano, R: rural): ')
a=2018-na
if cli>10 and hi>1:
      print('APROBADO')
elif (civ=='C' or civ=='c') and (hi>3) and (a>=45 and a<=55):
      print('APROBADO')
elif i>2500000 and (civ=='S' or civ=='s') and (hog=='U' or hog=='u'):
      print('APROBADO')
elif i>3500000 and cli>5:
      print('APROBADO')
elif (hog=='R' or hog=='r') and (civ=='C' or civ=='c') and hi<2:
      print('APROBADO')
else:
      print('RECHAZADO')