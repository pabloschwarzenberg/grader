#Aprobación de créditos
def calculo(años_pertenencia_banco, num_hijos, ingreso_pesos, año_nacimiento, estado_civil, vivienda):
    
    if años_pertenencia_banco >= 10 and num_hijos >= 2:

        print('APROBADO')
     
    else:

        print("RECHAZADO")
    
    if estado_civil == "C" and num_hijos <= 3 and año_nacimiento >= 1978 or año_nacimiento <= 1968:
        
        print('APROBADO')

    else:

        print("RECHAZADO")

    if ingreso_pesos >= 2500000 and estado_civil == "S" and vivienda == "U":
        
        print('APROBADO')
    
    else:

        print("RECHAZADO")

    if ingreso_pesos >= 3500000 and años_pertenencia_banco >= 5:

        print('APROBADO')

    else:

        print("RECHAZADO")

    if vivienda == "R" and estado_civil == "C" and num_hijos <= 2:

        print("APROBADO")

    else:

        print("RECHAZADO")


ingreso_pesos = int(input("ingresa el monto: "))
año_nacimiento = int(input("ingresa el año de nacimiento: "))
num_hijos = int(input("ingresa el número de hijos: "))
años_pertenencia_banco = int(input("ingresa la cantidad de años que has pertenecido al banco: "))
estado_civil = input("ingrese su estado civil, siendo 'C' casado y 'S' soltero: ")
vivienda = input("ingrese si vive en campo o ciudad, siendo 'U' urbano y 'R' rural:   ")

calculo(años_pertenencia_banco, num_hijos, ingreso_pesos, año_nacimiento, estado_civil, vivienda)