#Aprobación de créditos
A=eval(input("ingrese los ingresos en pesos:"))
B=eval(input("ingrese el año de nacimiento:"))
C=eval(input("ingrese la cantidad de hijos:"))
D=eval(input("ingrese los años en el banco:"))
E=input("casado (C) o soltero (S):")
F=input("urbano (U) o rural (R):")
edad=2020-B
if (D>10 and C>=2):
    print('APROBADO')
elif (E=="C" and B>3 and edad >=45 and edad <=55):
    print('APROBADO')
elif (A>3500000 and D>5):
    print('APROBADO')
elif (A>2500000 and E=="S" and F=="U"):
    print('APROBADO')
elif (F=="R" and E=="C" and C<2):
    print('APROBADO')
else:
    print('RECHAZADO')