#Aprobación de créditos
ingreso=int(input("ingreso:"))
año=int(input("año de nacimiento:"))
numero_de_hijos=int(input("numero de hijos:"))
presencia=int(input("años de presencia en el banco:"))
estado_civil=str(input("estado civil:"))
residencia=str(input("donde vive:"))

edad = 2021 - año

if presencia>=10:
    print("APROBADO")
elif numero_de_hijos>=2:
    print("APROBADO")
elif estado_civil==("casado"):
    print("APROBADO") 
elif edad==45:
    print ("APROVADO")
elif edad==55: 
    print("APROVADO")
elif ingreso>2500000:
    print("APROBADO")
elif ingreso>3500000:
    print("APROVADO")
elif presencia>5:
    print("APROVADO")
elif residencia==("campo"):
    print("APROBADO")
elif numero_de_hijos<2:
    print("APROVADO")
elif estado_civil==("SOLTERO"):
    print("aprovado")
elif residencia==("ciudad"):
    print("APROBADO")