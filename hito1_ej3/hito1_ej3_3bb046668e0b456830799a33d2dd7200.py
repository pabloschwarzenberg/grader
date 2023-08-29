#Aprobación de créditos
def aprobar_credito(ingreso, nacimiento, num_hijos, pertenencia, estado_civil, ubicacion):
    if pertenencia>10 and num_hijos>=2:
        return "APROBADO"
    elif estado_civil=="C" and num_hijos>3 and nacimiento>=45 and nacimiento <= 55:
        return "APROBADO"
    elif ingreso>2500000 and estado_civil=="S" and ubicacion=="U":
        return "APROBADO"
    elif ingreso>3500000 and pertenencia>5:
        return "APROBADO"
    elif ubicacion=="R" and estado_civil=="C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"
ingreso=int(input("Ingrese su ingreso en pesos: "))
#Fin
nacimiento=int(input("Ingrese su año de nacimiento: "))
num_hijos=int(input("Ingrese el número de hijos: "))
pertenencia=int(input("Ingrese los años de pertenencia al banco: "))
estado_civil=input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion=input("Ingrese su ubicación (U para urbano, R para rural): ")
resultado=aprobar_credito(ingreso, nacimiento, num_hijos, pertenencia, estado_civil, ubicacion)
print("Resultado:", resultado)      