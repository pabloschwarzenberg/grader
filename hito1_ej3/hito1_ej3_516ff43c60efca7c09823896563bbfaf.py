#Aprobación de créditos
      def verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if (anos_pertenencia > 10 and num_hijos >= 2) or \
       (estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55) or \
       (ingreso > 2500000 and estado_civil == "S" and ubicacion == "U") or \
       (ingreso > 3500000 and anos_pertenencia > 5) or \
       (ubicacion == "R" and estado_civil == "C" and num_hijos < 2):
        return "APROBADO"
    else:
        return "RECHAZADO"

ingreso = int(input("Ingrese su ingreso mensual (en pesos): "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese el número de años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

resultado = verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)

print("Resultado:", resultado)
