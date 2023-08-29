#Aprobación de créditos
Ingreso = int(input('Introduzca sus ingresos: '))
AñoNacimiento = int(input('Ingrese su año de nacimiento: '))
NHijos = int(input('Ingrese su numero de hijos: '))
AñoPertenencia = int(input('Ingrese sus años de pertenencia al Banco: '))
EstadoCivil = input('Estado Civil ("S": soltero, "C": casado): ').upper()
Vivienda = input('Ingrese si vive en campo o ciudad ("U": urbano, "R": rural): ').upper()
Edad = 2022 - AñoNacimiento
print(Edad)
Resultado = ''
if AñoPertenencia > 10 and NHijos >= 2:
    Resultado = 'APROBADO'
elif (EstadoCivil == 'C' or EstadoCivil == 'CASADO') and NHijos > 3 and (Edad >= 45 or Edad <= 55):
    Resultado = 'APROBADO'
elif Ingreso > 2500000 and (EstadoCivil == 'S' or EstadoCivil == 'SOLTERO') and (Vivienda == 'U' or Vivienda == 'URBANO'):
    Resultado = 'APROBADO'
elif Ingreso > 3500000 and AñoPertenencia > 5:
    Resultado = 'APROBADO'
elif (Vivienda == 'R' or Vivienda == 'RURAL') and (EstadoCivil == 'C' or EstadoCivil == 'CASADO') and NHijos < 2:
    Resultado = 'APROBADO'
else:
    Resultado = 'RECHAZADO'
print(Resultado)