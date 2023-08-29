from os import system
system("cls")

def evaluar_credito(ingreso, anio_nacimiento, num_hijos, anios_banco, estado_civil, tipo_vivienda):
    
   if anios_banco > 10 and num_hijos >= 2:
        return True
   elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
        return True
   elif ingreso > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
        return True
   elif ingreso > 3500000 and anios_banco > 5:
        return True
   elif tipo_vivienda == "R" and estado_civil == "C" and num_hijos < 2:
        return True
   else:
    return False


ingreso = float(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
tipo_vivienda = input("Ingrese su tipo de vivienda (U para urbano, R para rural): ")

aprobado = evaluar_credito(ingreso, anio_nacimiento, num_hijos, anios_banco, estado_civil, tipo_vivienda)
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")      