#Aprobación de créditos
# Interfaz
print("                                   >>>Atención Créditos de Consumo<<<                                   ")
print("A continuación se le solicitarán sus datos para verificar si es apto para obtener un crédito de consumo.")
print("                                                                                                        ")

# Datos
ingreso = int(input("Ingrese su ingreso mensual en moneda CLP: "))
años = int(input("Ingrese su edad: "))
num_hijos = int(input("Ingrese cantidad de hijos que tiene: "))
año_banco = int(input("Ingrese cantidad de años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil ('S' Soltero, 'C' Casado): ")
residencia = input("Ingrese su lugar de residencia ('U' Urbano, 'R' Rural): ")

# Procesamiento
if año_banco > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 < años < 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and residencia == "U":
    print("APROBADO")
elif ingreso > 3500000 and año_banco > 5:
    print("APROBADO")
elif residencia == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")