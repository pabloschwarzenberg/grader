#Cálculo del dígito verificador de un rut
 import random

def generar_rut():

    claves = [2, 3, 4, 5, 6, 7]

    p1 = random.randint(1, 50)
    p2 = random.randint(1, 1000)
    p2 = "0" * (3 - len(str(p2))) + str(p2)
    p3 = random.randint(1, 1000)
    p3 = "0" * (3 - len(str(p3))) + str(p3)
    
    num_con_pts = str(p1) + "." + str(p2) + "." + str(p3)
    num_sin_pts = num_con_pts.replace(".", "")

    invertido = num_sin_pts[::-1]

    suma = 0

    for i in range(len(invertido)):
        suma += int(invertido[i]) * claves[(i % len(claves))]

    verificador = suma // 11
    verificador *= 11
    verificador += 11 - suma

    if verificador == 11:
        verificador = "0"
    elif verificador == 10:
        verificador = "K"
    else:
        verificador = str(verificador)

    return num_con_pts + "-" + verificador     