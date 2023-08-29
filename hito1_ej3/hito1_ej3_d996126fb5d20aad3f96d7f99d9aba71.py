#Aprobación de créditos
 
Ingreso=int(input('Ingrese su Ingreso mensual en pesos: '))
while Ingreso<0:
    Ingreso=int(input('El número ingresado es incorrecto. Ingrese nuevamente su Ingreso mensual en pesos: '))
    
Nacimiento=int(input('\nIngrese su año de nacimiento: '))
while Nacimiento<0 or len(str(Nacimiento))!=4:
    Nacimiento=int(input('El año ingresado es incorrecto. Ingrese nuevamente su año de nacimiento: '))

NumeroDeHijos=int(input('\nIngrese su número de hijos: '))
while NumeroDeHijos<0:
    NumeroDeHijos=int(input('El númer ingresado es incorrecto. Ingrese nuevamente su número de hijos: '))

TiempoEnBanco=int(input('\nIngrese sus años de pertenencia al Banco: '))
while TiempoEnBanco<0:
    TiempoEnBanco=int(input('El número ingresado es incorrecto. Ingrese nuevamente sus años de pertenencia al banco: '))

EstadoCivil=str(input('\nIngrese su estado civil: Ingrese S si es soltero o C si es casado: '))
while EstadoCivil!='S' and EstadoCivil!='C':
    EstadoCivil=str(input('La opción ingresada es incorrecta. Ingrese nuevamente su estado civil: '))

Vive=str(input('\nIngrese su urbanización: Ingrese U si vive en una comuna urbana o R si vive en una comuna rural: '))
while Vive!='U' and Vive!='R':
    Vive=str(input('La opción ingresada es incorrecta. Ingrese nuevamente su urbanización: '))

#APROBACION
    
if TiempoEnBanco>10 and NumeroDeHijos>=2 or EstadoCivil=='C' and NumeroDeHijos>3 and 45<=(2020-Nacimiento)<=55 or Ingreso>2500000 and EstadoCivil=='S' and Vive=='U' or Ingreso>3500000 and TiempoEnBanco>5 or Vive=='R' and EstadoCivil=='C' and NumeroDeHijos<2:
    print('\nSu crédito ha sido APROBADO')

else:
    print('\nSu crédito ha sido RECHAZADO')
    
    
    
    
    