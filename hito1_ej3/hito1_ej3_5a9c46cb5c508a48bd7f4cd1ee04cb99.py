#Aprobación de créditos

income=int(input('Ingreso (en pesos): '))
birthyear=int(input('Año de nacimiento: '))
kids=int(input('Número de hijos: '))
bankyears=int(input('Años de pertenencia al banco: '))
status=input('Estado civil("S":soltero, "C", casado): ')
area=input('Si vive en campo o ciudad("U": urbano,"R": rural): ')

edad=int(2017-birthyear)

#Condicionales

if bankyears>10 and kids>=2:
    print('APROBADO')
elif (status=='C' and kids>=3) and 45<=edad<=55:
    print('APROBADO')
elif (income>2500000 and status=='S') and area=='U':
    print('APROBADO')
elif income>3500000 and bankyears>5:
    print('APROBADO')
elif (area=='R' and status=='C') and kids<2:
    print('APROBADO')
else:
    print('RECHAZADO')
