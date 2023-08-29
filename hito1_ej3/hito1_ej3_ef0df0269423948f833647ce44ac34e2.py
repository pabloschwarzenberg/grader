#Aprobación de créditos
ingreso= int(input("Ingrese ingresos en pesos: "))
nacimiento= int(input("Ingrese año de nacimiento: "))
numero_hijos= int(input("Ingrese numero de hijos: "))
anos_banco= int(input("Ingrese años de pertenencia al banco: "))
estado_civil= str(input("Ingrese S como soltero, C como casado: "))
donde_vive = str(input("Ingrese donde vive R como rural, U como urbano: "))

def credito(ingreso, nacimiento, numero_hijos, anos_banco, estado_civil, donde_vive):

    if anos_banco >=10 and numero_hijos >=2:
        return print ("aprobado")
    elif estado_civil == "C" and numero_hijos >3 and (2021-nacimiento) >=45 and (2021-nacimiento) <=55:
        return print ("aprobado")
    elif ingreso >2500000 and estado_civil == "S" and donde_vive == "U":
        return print("aprobado")
    elif ingreso >3500000 and anos_banco >=5:
        return print("aprobado")
    elif donde_vive == "R" and estado_civil == "C" and numero_hijos <2:
        return print("aprobado")

    else: return print ("rechazado")


credito(ingreso, nacimiento, numero_hijos, anos_banco, estado_civil, donde_vive)