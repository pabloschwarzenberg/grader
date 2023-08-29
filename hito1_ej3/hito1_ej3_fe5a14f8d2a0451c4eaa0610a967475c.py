#Aprobación de créditos
def Proceso(ingreso,nacimiento,numerohijos,estadobanco,estadocivil,residencia):
  if estadobanco>10 and numerohijos>=2:
    print('Aprobado')

  if estadocivil=='C' and numerohijos>3 and 1978>=nacimiento>=1968:
    print('Aprobado')

  if ingreso>2500000 and estadocivil=='S' and residencia=='U':
    print('Aprobado')

  if ingreso>3500000 and estadobanco>5:
    print('Aprobado')
    
  if residencia=='R' and estadocivil=='C' and numerohijos<2:
    print('Aprobado')

#######################[MAIN

print('Bienvenido')
print('')
print('')
print('1.Solicitar un credito')
print('2.Salir')

while(1):
  op=int(input('Que desea hacer?: '))

  if op==1:
    print('Porfavor ingrese sus datos')
    ingr=int(input('Ingrese su ingreso: '))
    year=int(input('Ingrese su year de nacimiento: '))
    hijos=int(input('Cuantos hijos tiene?(ingrese valor numerico): '))
    banco=int(input('Cuantos years lleva con el banco?(Ingrese valor numerico): '))
    civil=input('Ingrese su estado civil(S si es soltero, C si es casado): ')
    res=input('Vive en campo o ciudad?(U si es ciudad, R si es campo): ')
  
    Proceso(ingr,year,hijos,banco,civil,res)
  
  
  if op==2:
    print('Adios!')
    break
