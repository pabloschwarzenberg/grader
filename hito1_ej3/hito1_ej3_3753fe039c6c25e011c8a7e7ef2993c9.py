#Aprobación de créditos
ingreso=int(input("introduzca su ingreso en pesos porfavor: "))
ano=int(input("ingrese su ano de nacimiento porfavor: "))
hijos=int(input("ingrese su numero de hijos porfavor:"))
ano_banco=int(input("ingrese los anos que lleva en el banco porfavor: "))
ec=str(input("Ingrese su estado civil. 's' para soltero , 'c' para casado:",)).lower()
lugar_vive=str(input("Si vive en campo o ciudad. 'u' para ciudad , 'r' para campo:",)).lower()
edad=2020-ano
if(ano_banco>10 and hijos>=2):
  print("APROBADO")
if(ec=='c' and hijos>3 and 45<edad<55):
  print("APROBADO")
if(ingreso>2500000 and ec=='s' and lugar_vive=='c'):
  print("APROBADO")
if(ingreso>3500000 and ano_banco>5):
  print("APROBADO")
if(lugar_vive=='r' and ec=='c' and hijos<2):
  print("APROBADO")      