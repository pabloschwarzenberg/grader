Ingreso= int(input('Indique su ingreso: '))
AñoDeNacimiento= int(input('Indique su año nacimiento: '))
NumeroDeHijos= int(input("Indique su numero de hijos: "))
AñosDePertenenciaAlBanco= int(input("Indique sus años de pertenencia al banco: "))
EstadoCivil= str(input('Indique su estado civil (C)asado/(S)oltero: '))
TipoDeVivienda= str(input("Indique su tipo de vivienda (U)rbano/(R)ural: "))
Resultado= (AñoDeNacimiento-2020)
if (AñosDePertenenciaAlBanco) >= 10 and (NumeroDeHijos) >= 2:
    print ("APROBADO")
else:
    print ('RECHAZADO')
if (EstadoCivil) == 'C' and (NumeroDeHijos) > 3 and (Resultado) >= 45 or (AñoDeNacimiento) <= 55:
    print ("APROBADO")
else:
    print ('RECHAZADO')
if (Ingreso) > 2500000 and (EstadoCivil) == 'S' and (TipoDeVivienda) == 'U':
    print ('APROBADO')
else:
    print ("RECHAZADO")
if (Ingreso) > 3500000 and (AñosDePertenenciaAlBanco) > 5:
    print ('APROBADO')
else:
    print('RECHAZADO')
if (TipoDeVivienda) == 'R' and (NumeroDeHijos) <= 2:
    print ('APROBADO')
else:
    print ('RECHAZADO')