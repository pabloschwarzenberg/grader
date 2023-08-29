#Aprobación de créditos
def aprobar_credito():
    ingreso = float(input("Ingrese su ingreso en pesos: "))
    nacimiento = int(input("Ingrese su año de nacimiento: "))
    hijos = int(input("Ingrese el número de hijos que tiene: "))
    banco = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    tipo_vivienda = input("Ingrese el tipo de vivienda (U para urbano, R para rural): ")

    if banco > 10 and hijos >= 2:
        return "APROBADO"
    
    if estado_civil == "C" and hijos > 3 and 45 <= (2023 - nacimiento) <= 55:
        return "APROBADO"
    
    if ingreso > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
        return "APROBADO"
    
    if ingreso > 3500000 and banco > 5:
        return "APROBADO"
    
    if tipo_vivienda == "R" and estado_civil == "C" and hijos < 2:
        return "APROBADO"
    
    return "RECHAZADO"

resultado = aprobar_credito()
print(resultado)
      