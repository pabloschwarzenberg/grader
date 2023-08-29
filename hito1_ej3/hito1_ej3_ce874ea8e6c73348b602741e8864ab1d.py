#Aprobación de créditos

Ingresos = float(input('Ingrese su ingreso en pesos chilenos: '))
AnoDeNacimiento = int(input('Ingrese su ano de nacimiento: '))
NHijos = int(input('Ingrese su numeo de hijos: '))
AnosPerteneciaAlBanco = int(input('Cuantos anos ha sidp parte del banco: '))
EstadoCivil = input('Ingrese su estado civil, soltero (S), o casado (C): ')
Residencia = input('Vive en una zona urbana (U) o rural (R): ')

Aprobado = False

while True: 
    if AnosPerteneciaAlBanco > 10 and NHijos >= 2:
        Aprobado = True
        break

    elif (EstadoCivil == 'C' or EstadoCivil == 'c') and NHijos > 3 and ((2023 - AnoDeNacimiento) >= 45 and (2023 - AnoDeNacimiento) <= 55):
        Aprobado = True
        break

    elif Ingresos > 2500000 and (EstadoCivil == 'S' or EstadoCivil == 's') and (Residencia == 'U' or Residencia == 'u'):
        Aprobado = True
        break

    elif Ingresos > 3500000 and AnosPerteneciaAlBanco > 5:
        Aprobado = True
        break

    elif (Residencia == 'U' or Residencia == 'u') and (EstadoCivil == 'C' or EstadoCivil == 'c') and NHijos < 2:
        Aprobado == True
        break
    else:
        break

if Aprobado == True:
    print('APROBADO')

else:
    print('RECHAZADO')