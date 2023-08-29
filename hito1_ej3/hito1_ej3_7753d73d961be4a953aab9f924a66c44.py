ingreso=int(input("cual es su ingreso:"))
ano=int(input("ingrese su año de nacimiento:"))
hijos=int(input("cuantos alos tiene:"))
permanencia=int(input("cuantos años tiene en el banco"))
estadocivil=str(input("¿cual es su estado civil? C=casado , S=soltero"))
vivienda=str(input("¿vive en el campo o ciudad? U=urbano , R=rural"))
edad=2022-ano
if permanencia>10 and hijos>=2 or estadocivil=="C" and hijos>1 and edad==45 or ingreso>3500000 and permanencia>5 or vivienda=="R" and estadocivil=="C" and hijos<2:
  print("APROBADO")
else:
  print("REPROBADO")
  