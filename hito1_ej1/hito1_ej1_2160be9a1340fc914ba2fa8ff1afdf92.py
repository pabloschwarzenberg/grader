pt = float(input('¿Cual es tu nota de tareas? '))
pi = float(input('Cual es tu nota de interrogaciones? '))
ne = float(input('¿Cual es tu nota de examen? '))
pp = float(input('¿Cual es tu nota de presentacion? '))

pt_1 = float(pt * 0.3)
pi_1 = float(pi * 0.3)
ne_2 = float(ne * 0.3)
pp_1 = float(pp * 0.1)

suma = round(pt_1 + pi_1 + ne_2 + pp_1 , 2)
print(suma)