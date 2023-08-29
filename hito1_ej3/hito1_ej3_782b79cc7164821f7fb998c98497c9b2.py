Ingresos=int(input('Ingrese pesos: '))
Año=int(input('Ingrese año de nacimiento: '))
Hijos=int(input('Ingrese cuantos hij@s tiene: '))
Añospertenencia=int(input('Cuantos años lleva en este banco: '))
EstadoCivil=input('Para soltero ingrese S, para casado ingrese C: ')
Vivienda=input('Urbana ingrese U, rural ingrese R: ')
Edad=2023-Año
if Año>10 and Hijos>=2:
  print('APROBADO')
elif EstadoCivil=='C' and Hijos>3 and Edad>=45 and Edad<=55:
  print('APROBADO')
elif Ingresos>2500000 and EstadoCivil=='S' and Vivienda=='U':
  print('APROBADO')
elif Ingresos>3500000 and Añospertenencia>5:
  print('APROBADO')
elif Vivienda=='R' and EstadoCivil=='C' and Hijos<2:
  print('APROBADO')
else:
  print('REPROBADO')