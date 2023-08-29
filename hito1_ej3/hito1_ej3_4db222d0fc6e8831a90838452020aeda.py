#Aprobación de créditos
Ingresos= int(input('ingresar ingresos en pesos:'))
año_de_nacimiento=int(input('ingresar año de nacimiento:'))
Numero_hijos=int(input('ingresar numero de hijos:'))
Año_de_pertenencia_al_banco=int(input('ingresar numero de años que pertenece al banco'))
Estado_civil=input('ingresar estado civil "S" o "C":')
Vive=input('ingrese lugar donde vive "U" o R":')
R='Campo'
U='Ciudad'
C='Casado'
S='Soltero'

if (Año_de_pertenencia_al_banco>10)and(Numero_hijos>=2):
     print('Aprobado')

if (Estado_civil==C)and(Numero_hijos>3)and(45>=(2018-Año_de_nacimiento)<=55):
     print('Aprobado')

if (Ingresos>2500000)and(Estado_civil==S)and(Vive==U):
     print('Aprobado')

if (Ingresos>3500000)and(Año_de_pertenencia_al_banco>5):
     print('Aprobado')

if (Vive==R)and(Estado_civil==C)and(Numero_hijos<2):
     print('Aprobado')

else:
   print('Rechazado')      