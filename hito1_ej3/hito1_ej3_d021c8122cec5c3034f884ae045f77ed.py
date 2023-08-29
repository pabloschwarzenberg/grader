#Aprobación de créditos
ingreso=int(input('Ingresos (en pesos): '))
AñodeN=int(input('Ingrese su año de nacimiento: '))
Ndehijos=int(input('Ingrese su numero de hijos: '))
AñosdeP=int(input('Ingrese cuantos años tiene de pertenencia al banco: '))
EstadoC=input('Ingrese su Estado Civil ("S": soltero, "C": casado) : ')
Vive=input('Ingrese donde vive ("U": urbano, "R":rural): ')

if AñosdeP>10 and Ndehijos>=2:
    print('APROBADO')
    
elif EstadoC=='C' and Ndehijos>3 and AñodeN>1964 and  AñodeN<1976:
    print('APROBADO')

elif ingreso>2500000 and EstadoC=='S' and Vive=='U':
    print('APROBADO')

elif ingreso>3500000 and AñosdeP>5:
    print('APROBADO')

elif Vive=='R' and EstadoC=='C' and Ndehijos<2:
    print('APROBADO')
else:
    print('RECHAZADO')
      