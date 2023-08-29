#Aprobación de créditos
ingresos = int(input('Ingrese sus ingresos en pesos Chilenos: '))
año_nacimiento = int(input('Ingrese su año de nacimiento: '))
numero_hijos = int(input('Ingrese cuántos hijos tiene: '))
años_banco = int(input('Ingrese los años que ha permanecido en el banco: '))
edad = (2021 - año_nacimiento)

estado_civil = input('Ingrese su estado civil, S=solter@ o C=casad@:')

zona = input('¿Vive en zonas rurales(R) o urbanas(U)?:')


if (años_banco > 10) and (numero_hijos >= 2):
    print('APROBADO')
elif (estado_civil == 'C' or 'c') and (numero_hijos > 3) and (edad >= 45) and (edad <= 55):
    print('APROBADO')
elif (estado_civil == 'S' or 's') and (zona == 'U' or 'u') and (ingresos > 2500000):
    print('APROBADO')
elif (ingresos > 3500000) and (años_banco > 5):
    print('APROBADO')
elif (estado_civil == 'C' or 'c') and (numero_hijos < 2) and (zona == 'R' or 'r'):
    print('APROBADO')
else:
    print('RECHAZADO')