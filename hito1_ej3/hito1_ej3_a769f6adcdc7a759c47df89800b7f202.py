#Aprobación de créditos
sueldo = eval(input('Ingrese su sueldo: '))
Edad = int(input('Ingrese su año de nacimiento: '))
hijos = int(input('Ingrese cuantos hijos tiene: '))
permanencia = int(input('Ingrese años de pertenencia al banco: '))
estado = str(input('Ingrese su estado civil: '))
vive = str(input('Ingrese si vive en el campo o ciudad: '))

Edad == 2020 - Edad



if permanencia > 10 and hijos >= 2:
  print('APROBADO')
  
elif (estado == 'C') and (hijos > 3) and ((Edad >=45) and (Edad <= 55)):
  print('APROBADO')
  
elif sueldo > 2500000 and estado == 'S' and vive == 'U':
    print('APROBADO')

elif sueldo > 3500000 and permanencia > 5:
    print('APROBADO')

elif vive == 'R' and estado == 'C' and hijos < 2:
    print('APROBADO')

else:
    print('RECHAZADO')
