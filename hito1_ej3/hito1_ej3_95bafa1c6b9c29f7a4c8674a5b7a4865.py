#Aprobación de créditos
ingresos = eval(input("Ingresos en pesos:"))
ano = eval(input("Año de nacimiento:"))
hijos = eval(input("Número de hijos:"))
pertenencia = eval(input("Años de pertenencia al banco:"))
estadocivil =  input("Ingrese su Estado Civil S para Soltero y C para Casado:")

domicilio = input("Ingrese lugar de domicilio U para Urbano y R para Rural:")

edad = 2022 - ano

if pertenencia >= 10 and hijos >= 2:
    print("APROBADO")
elif estadocivil == 'C' and hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif estadocivil == 'S' and ingresos > 2500000 and domicilio == 'U':
    print("APROBADO")
elif ingresos > 3500000 and permanencia > 5:
    print("APROBADO")
elif domicilio == 'R' and estadocivil =='C' and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")