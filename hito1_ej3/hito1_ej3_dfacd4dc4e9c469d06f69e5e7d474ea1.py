#Aprobación de créditos
ingreso=int(input('Ingrese sus ingresos en pesos: '))
nacimiento=int(input('Ingrese su año de nacimiento: '))
hijos=int(input('Ingrese su numero de hijos: '))
año=int(input('Ingrese sus años de pertenencia en el banco: '))
estado=str(input('Ingrese "S": soltero o "C":casado '))
area=str(input('Ingrese "U":urbano o "R":rural '))

if (año>10 and hijos>=2):
    print("APROBADO")
elif (estado=="C" and hijos>3 and 1963<=nacimiento<=1973 ):
    print("APROBADO")
elif (ingreso>2500000 and estado=="S" and area=="U"):
    print("APROBADO")
elif (ingreso>3500000 and año>5):
    print("APROBADO")
elif (area=="R" and estado=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")