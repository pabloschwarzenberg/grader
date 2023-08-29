#Aprobación de créditos
print('Ingrese los siguientes datos para saber si cumple con los requisitos para optar a un credito de consumo')
ingresos=eval(input('Ingresos en pesos:$ ' ))
año=eval(input('Año de nacimiento:  '))
hijos=eval(input('Numero de hijos: '))
añosenelbanco=eval(input('Años de permanencia al banco: '))
estado=input('Estado civil "S": soltero/a // "C":casado/a: ')
vive=input('Vivienda en ¿ciudad o campo? "U": urbano // "R": rural: ')
edad=2020-año
if(añosenelbanco>10 and hijos>=2):
          print('APROBADO')
elif(estado=="C" and hijos>3 and edad>=45 and edad<=55):
          print('APROBADO')
elif(ingresos>2500000 and estado=="s" and vive=="U"):
          print('APROBADO')
elif(ingresos>3500000 and añosenelbanco>5):
          print('APROBADO')
elif(vive== "R" and estado=="C" and hijos<2):
          print('APROBADO')
else:
          print('RECHAZADO')    