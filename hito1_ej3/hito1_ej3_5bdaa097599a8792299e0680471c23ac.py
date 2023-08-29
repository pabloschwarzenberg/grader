ingreso=int(input('ingreso ne pesos chilenos'))
nacimiento=int(input('Año de nacimiento'))
hijos=int(input('numero de hijos'))
banco=int(input('años pertenecientes al banco'))
estado=str(input('S,soltero o C, casado'))
ciudad=str(input('¿vive en campo o cuidad U, urbano o R, rural'))
nacimiento=2018-nacimiento
S=estado
C=estado
R=ciudad
U=ciudad


if banco>10 and hijos>=2:
    print('APROBADO')
elif hijos>=3 and nacimiento >= 45 and nacimiento <= 55 and estado == C:
    print('APROBADO')
elif ingreso > 2500000 and estado==S and ciudad==U:
    print('APROBADO')
elif ingreso>3500000 and banco>5:
    print('APROBADO')
elif ciudad == R and estado== C and hijos <= 2 and hijos >= 0:
    print('APROBADO')
else:
    print("RECHAZADO")
