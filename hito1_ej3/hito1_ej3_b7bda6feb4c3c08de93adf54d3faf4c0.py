def verificar_aprobacion(ingreso, año_nacimiento, num_hijos, años_banco, estado_civil, ubicacion):
    if años_banco > 10 and num_hijos >= 2:
        return True
    
    if estado_civil == 'C' and num_hijos > 3 and 45 <= (2023 - año_nacimiento) <= 55:
        return True
    
    if ingreso > 2500000 and estado_civil == 'S' and ubicacion == 'U':
        return True
    
    if ingreso > 3500000 and años_banco > 5:
        return True
    
    if ubicacion == 'R' and estado_civil == 'C' and num_hijos < 2:
        return True
    
    return False

ingreso = int(input("Ingrese su ingreso en pesos: "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
años_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

aprobado = verificar_aprobacion(ingreso, año_nacimiento, num_hijos, años_banco, estado_civil, ubicacion)

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
