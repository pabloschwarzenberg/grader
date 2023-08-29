ingresos = int(input("ingrese su salario: "))
ano_nacimiento=int(input("año de nacimiento: "))
numero_hijos=int(input("cantidad de hijos: "))
anos_banco = int(input("cuantos años lleva con el banco: "))
estado_civil = str(input("Su estado civil: "))
donde_vive = str(input("Donde vive: "))
if anos_banco > 10 and numero_hijos >= 2 or estado_civil == 'C' and numero_hijos > 3 and ano_nacimiento > (ano_nacimiento-45)  and (ano_nacimiento < ano_nacimiento - 55) or ingresos > 2500000 and estado_civil == 'S' and donde_vive == 'U'or donde_vive == 'R' and estado_civil == 'C' and numero_hijos <2:
    print("APROBADO")

else:
    print("NO APROBADO")     