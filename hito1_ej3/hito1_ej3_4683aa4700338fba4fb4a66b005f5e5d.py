def aprobacion_creditos(ing, nac, hijos, pert, ec, lugar):
    edad = 2023 - nac

    if pert > 10 and hijos >= 2:
        return True

    elif ec == 'C' and hijos > 3 and (edad >= 45 and edad <= 55):
        return True
    
    elif ing > 2500000 and ec == 'S' and lugar == 'U':
        return True

    elif ing > 3500000 and pert > 5:
        return True

    elif lugar == 'R' and ec == "C" and hijos < 2:
        return True

    else:
        return False    

ingresos = int(input())
nacimiento = int(input())

cantidad_hijos = int(input())
pertenencia = int(input())
estado_civil = input() # S / C
lugar = input() # U / R

if aprobacion_creditos(ingresos, nacimiento, cantidad_hijos, pertenencia, estado_civil, lugar):
    print('APROBADO')

else:
    print('RECHAZADO')

