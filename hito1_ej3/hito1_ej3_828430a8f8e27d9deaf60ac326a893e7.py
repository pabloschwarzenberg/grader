print('bienvenido al banco masterplop, ingrese sus datos para saber si cumple con los requisitos para un credito de consumo')
ingresos=eval(input('comunique sus ingresos en peso: ' ))
año=eval(input('ingrese su año de nacimiento: '))
hijos=eval(input('ingrese su numero de hijos: '))
apb=eval(input('ingrese sus años de pertenencia al banco: '))
estado=input('ingrese su estado civil: "S": solter@ // "C", casad@: ')
vive=input('vivienda en ¿ciudad o campo? "U": urbano // "R": rural: ')
edad=2020-año
if(apb>10 and hijos>=2):
          print('APROBADO')
elif(estado.upper()=='C' and hijos>3 and edad>=45 and edad<=55):
          print('APROBADO')
elif(ingresos>2500000 and estado.upper()=='S' and vive.upper()=='U'):
          print('APROBADO')
elif(ingresos>3500000 and apb>5):
          print('APROBADO')
elif(vive.upper()=='R' and estado.upper()=='C' and hijos<2):
          print('APROBADO')
else:
          print('RECHAZADO')
