#Aprobación de créditos
continua = True
while continua:
    ingreso = int(input('ingreso en pesos: '))
    año_nacimiento = int(input('ingrese su año de nacimiento: '))
    edad = 2023 - año_nacimiento
    numero_de_hijos = int(input('ingrese numero de hijos: '))
    años_banco = int(input('ingrese años de pertenencia al banco: '))
    e_civil = str(input('ingrese estado civi(S: soltero, C : casado )'))
    if e_civil == 'S':
        continua = True
    elif e_civil == 'C':
          continua = True
    else:
        print('dato ingresado es incorrecto')
        break
    localidad = str(input('Vive en campo o ciudad (U: Urbano, R: Rural)'))
    if localidad == 'U':
        continua = True
    elif localidad == 'R':
        continua = True
    else:
        print('dato ingresado incorrecto')
        break
    if años_banco > 10 and numero_de_hijos >= 2:
        print('APROBADO')
        continua = False
    elif e_civil == 'S' and numero_de_hijos > 3 and (edad > 45 and edad < 55):
        print('APROBADO')
        continua = False
    elif ingreso > 2500000 and e_civil == 'S' and localidad == 'U':
        print('APROBADO')
        continua = False
    elif ingreso > 3500000 and años_banco > 5:
        print('APROBADO')
        continua = False
    elif localidad == 'R' and e_civil == 'C' and numero_de_hijos < 2:
        print('APROBADO')
        continua = False
    else:
        print('Rechazado')
        continua = False    