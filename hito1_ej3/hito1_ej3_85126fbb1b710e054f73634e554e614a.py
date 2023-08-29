#Aprobación de créditos
ingreso= int(input("ingreso en pesos :"))
años= int(input("año de nacimiento :"))
hijos= int(input("numero de hijos :"))
año_banco= int(input("años en el banco :"))
estado_civil= input("estado civil(S:soltero, C:casado): ")
donde_vive= input("lugar donde vive (U:urbano, R:rural) :")

if ((año_banco>10 and hijos >=2) or (estado_civil=="C" and hijos>3 and 45>=años>=55) or (ingreso>2500000 and estado_civil=="S" and donde_vive=="U") or (ingreso>3500000 and año_banco>5) or (donde_vive=="R" and estado_civil=="C" and hijos<2)):
    print("APROBADO")
else:
    print("RECHAZADO")

