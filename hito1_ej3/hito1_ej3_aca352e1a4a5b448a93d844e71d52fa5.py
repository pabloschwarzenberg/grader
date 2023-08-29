# Algorito de aprobacion de creditos
from datetime import date
from datetime import datetime

monto_pesos = 0
ano_nacimiento = 0
cantidad_hijos = 0
antiguedad_banco = 0
estado_civil = "N"
tipo_vivienda = "N"
ano_actual = int(format(date.today().year))


# Valida monto en pesos.
entrada = input("Ingrese monto de ingresos en pesos : ")
control = True
while control:
    # Evalua que corresponda a un valor numerico y que se mayor que 0.
    if entrada.isnumeric() and int(entrada) > 0:
        monto_pesos = int(entrada)
        control = False
    else:
        entrada = input(
            "Valor incorrecto, Ingrese monto de ingresos en pesos : ")


# Valida año de nacimiento.
entrada = input("Ingrese año de nacimiento : ")
control = True
while control:
    # Evalua que corresponda a un valor numerico y que se mayor que 0.
    if entrada.isnumeric() and int(entrada) > 0 and int(entrada) <= ano_actual:
        ano_nacimiento = int(entrada)
        control = False
    else:
        entrada = input("Valor incorrecto, Ingrese año de nacimiento : ")


# Valida numero de hijos.
entrada = input("Ingrese numero de hijos : ")
control = True
while control:
    # Evalua que corresponda a un valor numerico y que se mayor que 0.
    if entrada.isnumeric() and int(entrada) > 0:
        cantidad_hijos = int(entrada)
        control = False
    else:
        entrada = input("Valor incorrecto, Ingrese numero de hijos : ")


# Valida antiguedad en banco.
entrada = input("Ingrese numero de años de antiguedad en banco : ")
control = True
while control:
    # Evalua que corresponda a un valor numerico y que se mayor que 0.
    if entrada.isnumeric() and int(entrada) > 0:
        antiguedad_banco = int(entrada)
        control = False
    else:
        entrada = input(
            "Valor incorrecto, Ingrese numero de años de antiguedad en banco : ")


# Valida estado civil.
entrada = input("Ingrese estado Civil S=Soltero/C=Casado : ")
control = True
while control:
    # Evalua que corresponda a un valor numerico y que se mayor que 0.
    if entrada.upper() in 'CS':
        estado_civil = entrada.upper()
        control = False
    else:
        entrada = input(
            "Valor incorrecto, Ingrese estado Civil S=Soltero/C=Casado : ")


# Valida tipo de vivienda.
entrada = input("Ingrese tipo de vivienda U=Urbana/R=Rural : ")
control = True
while control:
    # Evalua que corresponda a un valor numerico y que se mayor que 0.
    if entrada.upper() in 'UR':
        tipo_vivienda = entrada.upper()
        control = False
    else:
        entrada = input(
            "Valor incorrecto, Ingrese tipo de vivienda U=Urbana/R=Rural : ")

# Fin de bloque de validacion de datos de entrada.

# Evalua condiciones del credito.

# Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if antiguedad_banco > 10 and cantidad_hijos >= 2:
    print("APROBADO")
# Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif estado_civil == "C" and cantidad_hijos > 3 and 45 <= (ano_actual - ano_nacimiento) <= 55:
    print("APROBADO")
# Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif monto_pesos > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
    print("APROBADO")
# Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif monto_pesos > 3500000 and antiguedad_banco > 5:
    print("APROBADO")
# Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif tipo_vivienda == "R" and estado_civil == "C" and cantidad_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO ")
