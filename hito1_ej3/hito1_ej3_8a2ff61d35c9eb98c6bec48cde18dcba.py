#Aprobación de créditos
print('        SOLICITUD DE CRÉDITOS   ')

IN = int(input('Ingrese el monto de sus ingresos (CLP): '))
NAC = int(input('¿En qué año nació?: '))
HI = int(input('¿Cuántos hijos tiene?: '))
ABO = int(input('¿Hace cuántos años se unió a nuestro banco?: '))
EC = input('Estado civil; S para soltero, C para casado: ')
VV = input('¿Vive en sector urbano(U) o rural(R)?: ')
ed = 2022-NAC
U = 'urbano'
R = 'rural'
S = 'soltero'
C = 'casado'
a = 'APROBADO'
r = 'RECHAZADO'
if ABO>10 and HI>=2:
    print(a)
elif EC==C and (HI>3) and (45<=(2022-NAC)<=55):
      print(a)
elif (IN>250000) and (EC==S) and (VV==U):
    print(a)
elif ((IN>350000) and (ABO>5)):
    print(a)
elif ((VV==R) and (EC==C) and (HI<=1)):
    print(a)
else:
    print(r)