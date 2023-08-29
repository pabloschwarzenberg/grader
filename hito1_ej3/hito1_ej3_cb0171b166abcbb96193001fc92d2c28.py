S = 1
C = 2 
U = 1
R = 2

ingresos = int(input('ingrese ingresos en pesos:'))
año = int(input('ingrese año de nacimiento:'))
hijos = int(input('ingrese numero de hijos:'))
añosdebanco = int(input('ingrese años de pertenencia al banco:'))
estadoc = eval( input('ingrese estado civil, "S": soltero, "C": casado:'))
vive = eval(input('a donde pertenese, "U": urbano, "R": rural:')) 


if añosdebanco > 10 and 2<= hijos:
 print('El credito es APROBADO')
if estadoc == 2 and hijos >=3 and  45 <=añosdebanco<=55:
 print('El credito es APROBADO')
if  ingresos >= 2500000 and  estadoc== 1 and  vive == 2:
 print('El credito es APROBADO')
if ingresos >= 3500000 and  añosdebanco >= 5:    
 print('El credito es APROBADO')
if  vive == 2 and estadoc == 2 and 2 > hijos:
 print('El credito es APROBADO')

else:
 print('El credito fue RECHAZADO')
