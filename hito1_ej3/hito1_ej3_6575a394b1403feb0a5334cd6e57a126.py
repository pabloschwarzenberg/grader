#Aprobacion credito del banco
ingresos = int(input('Ingreso:' ))
nacimiento = int(input('Año de nacimiento:' ))
hijos = int(input('Numero de hijos:' ))
añosbanco = int(input('Años como cliente:' ))
estadocivil = str(input('Estado civil (S soltero C casado):'  ))
casa = str(input('Vivienda (U urbano R rural):' ))
edad = 2020 - nacimiento
if (añosbanco >= 10) and (hijos >= 2):
    print('APROBADO')
elif (estadocivil == 'C') and (hijos >= 3) and (45 <= edad <= 55):
    print('APROBADO')
elif (ingresos >= 2500000) and (estadocivil == 'S') and (casa == 'U'):
    print('APROBADO')
elif (ingresos >= 3500000) and (añosbanco > 5):
    print('APROBADO')
elif (casa == 'R') and (estadocivil == 'C') and (hijos <= 2):
    print('APROBADO')
else:
    print('RECHAZADO')
      