#Aprobación de créditos
      #BANCO

INGRESO = int(input("Ingrese su ingreso (en pesos) : "))
NACIMIENTO = int(input("Ingrese su año de nacimiento : "))
NUM_HIJOS = int(input("Ingrese la cantidad de hijos que tiene :  "))
ANIOS_EN_BANCO = int(input("Años de pertenencia al banco :  "))
ESTADO_CIVIL = input("Estado civil: 'S' Soltero / 'C' Casado : ")
UBICACION = input("'U' Urbano / 'R' Rural : ")


if ANIOS_EN_BANCO>10 and NUM_HIJOS>=2:
    print("APROBADO")

elif (ESTADO_CIVIL=='C' or ESTADO_CIVIL=='c') and (NUM_HIJOS>3) and (((2022-NACIMIENTO)<55) and ((2022-NACIMIENTO)>45)):
    print("APROBADO")

elif (INGRESO>2500000) and (ESTADO_CIVIL=='S' or ESTADO_CIVIL=="s") and (UBICACION=='U' or UBICACION=='u'):
    print("APROBADO")

elif (INGRESO>3500000) and (ANIOS_EN_BANCO>5):
    print("APROBADO")

elif (UBICACION=='C' or UBICACION=='c') and (ESTADO_CIVIL=='C' or ESTADO_CIVIL=='c') and (NUM_HIJOS<2):
    print("APROBADO")

else:
    print("RECHAZADO")