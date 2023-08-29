#Aprobación de créditos
      ingreso = int(input("ingreso: "))
año = int(input("año de nacimiento: "))
hijos = int(input("número de hijos: "))
años_banco = int(input("años afiliado al banco: "))
estado_civil = str(input("estado civil: "))
donde_vive = str(input("donde vive: "))
edad = 2021 - año 
if años_banco>=10:
    print("APROBADO")
elif hijos>=2:
    print("APROBADO")
elif estado_civil==("casado"):
    print("APROBADO") 
elif edad==45:
    print ("RECHAZADO")
elif edad==55: 
    print("RECHAZADO")
elif ingreso>2500000:
    print("APROBADO")
elif ingreso>3500000:
    print("RECHAZADO")
elif años_banco>5:
    print("RECHAZADO")
elif donde_vive==("campo"):
    print("APROBADO")
elif hijos<2:
    print("RECHAZADO")
elif estado_civil==("SOLTERO"):
    print("RECHAZADO")
elif donde_vive==("ciudad"):
    print("APROBADO")