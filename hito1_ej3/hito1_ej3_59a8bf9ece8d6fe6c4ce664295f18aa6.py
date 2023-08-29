salario = int(input("Digite su ingreso mensual: '"))
nacimiento = int(input("Ingrese su año de nacimiento: "))
nacimiento = 2020 - nacimiento
hijos = int(input("Ingrese cantidad de hjos: "))
pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
estado = input("Ingrese su estado civil, 'S' si es solter@, 'C' si es casad@: ")
vive = input("Indique si vive en campo con una 'U' o en ciudad con una 'R': ")

if pertenencia > 10 and hijos >= 2:
    print('APROBADO')
elif estado == 'C' and hijos > 3 and nacimiento1 >= 45 and Nacimiento <= 55:
    print('APROBADO')
elif salario > 2500000 and estado == 'S' and vive == 'U':
    print('APROBADO')
elif salario > 3500000 and pertenencia > 5:
    print('APROBADO')
elif vive == 'R' and estado == 'C' and hijos < 2:
    print('APROBADO')
elif salario > 3500000 and pertenencia > 5:
    print('APROBADO')
elif vive == 'R' and estado == 'C' and hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')