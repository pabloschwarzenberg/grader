#Aprobación de créditos
def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, lugar_residencia):
    edad = 2023 - ano_nacimiento

    if anos_banco > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and 45 <= edad <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return True
    elif ingreso > 3500000 and anos_banco > 5:
        return True
    elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

# Solicitar al cliente que ingrese los datos
ingreso = float(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
lugar_residencia = input("Ingrese si vive en campo o ciudad (U: urbano, R: rural): ")

# Verificar la aprobación del crédito llamando a la función
aprobado = aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, lugar_residencia)

# Imprimir el resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")      