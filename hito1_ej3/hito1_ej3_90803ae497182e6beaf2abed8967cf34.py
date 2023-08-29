#aprobacion de creditos
#variables
s = "soltero"
c = "casado"
r = "campo"
k = "ciudad"
#entradas
ingreso = int(input("ingreso en pesos: "))
año = int(input("año de nacimiento: "))
hijos = int(input("numero de hijos: "))
banco = int(input("años en el banco: "))
estado = input("estado civil(coloque s para soltero o c para casado): ")
domicilio = input("domicilio(si vive en campo coloque r, si vive en ciudad coloque k): ")
#condiciones

if banco>=10 and hijos>=2:
    print("APROBADO")
else: print("RECHAZADO")

if c and hijos>=3 and 45<=año<=55:
    print("APROBADO")
else: print("RECHAZADO")
        
if ingreso>=2500000 and s and k:
    print("APROBADO")
else: print("RECHAZADO")

if ingreso>=3500000 and banco>=5:
    print("APROBADO")
else: print("APROBADO")

if r and c and hijos<=2:
    print("APROBADO")
else: print("RECHAZADO")