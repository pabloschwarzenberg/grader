ingreso = int(input("ingreso:"))
ano = int(input("año de nacimiento:"))
numero_hijos = int(input("numero de hijos:"))
pertenencia_banco = int(input("años de presencia en el banco:"))
estado_civil = str(input("estado civil:"))
cede = str(input("donde vive:"))
edad = 2021 - ano 
if pertenencia_banco>=10:
    print("APROBADO")
elif numero_hijos>=2:
    print("APROBADO")
elif edad==("casado"):
    print("APROBADO") 
elif edad==45:
    print ("APROBADO")
elif edad==55: 
    print("APROBADO")
elif ingreso>2500000:
    print("APROBADO")
elif ingreso>3500000:
    print("APROBADO")
elif pertenencia_banco>5:
    print("APROBADO")
elif cede==("campo"):
    print("APROBADO")
elif numero_hijos<2:
    print("APROBADO")
elif estado_civil==("SOLTERO"):
    print("APROBADO")
elif cede==("ciudad"):
    print("APROBADO")