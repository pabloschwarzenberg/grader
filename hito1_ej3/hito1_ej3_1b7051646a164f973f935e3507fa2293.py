#Entrada
ingreso           = int(input('Ingrese sus ingresos :'))
nacimiento        = int(input('Ingrese su fecha de nacimiento :'))
num_hijos         = int(input('Ingrese numero de hijos :'))
pertenencia_banco = int(input('Ingrese años de pertenencia al banco :'))
estado_civil      = input('C: Casado , S: Soltero :')
lugar             = input('U: Urbano , R: Rural :')

#Obtenemos la inicial 
estado_civil = str(estado_civil)[:1]
lugar = str(lugar)[:1]

#Calculamos la edad
edad = 2021 - nacimiento

#Generamos las condiciones
if pertenencia_banco > 10 and num_hijos > 2 :
    mensaje = 'APROBADO'
elif estado_civil == 'c' or estado_civil == 'C' and num_hijos > 3 and edad >= 45 or edad <= 55 : 
        mensaje = 'APROBADO'
        if ingreso > 2500000 and estado_civil == 'S' or estado_civil == 's' and lugar == 'U' or lugar == 'u' :
            mensaje = 'APROBADO'
            if ingreso > 3500000 and pertenencia_banco > 5 :
                mensaje = 'APROBADO'
                if lugar == 'R' or lugar == 'r' and estado_civil == 'C' or estado_civil == 'c' and num_hijos < 2 :
                    mensaje = 'APROBADO'
else : 
    mensaje = 'RECHAZADO'


print(mensaje)