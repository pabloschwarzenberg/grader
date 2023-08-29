#Aprobación de créditos
ing = int(input("ingreso:"))
agn = int(input("año de nacimiento:"))
nmr = int(input("numero de hijos:"))
prs = int(input("años de presencia en el banco:"))
est = str(input("estado civil:"))
dnv = str(input("donde vive:"))

edad = 2021 - agn

if prs>=10:
    print("APROBADO")
elif nmr>=2:
    print("APROBADO")
elif est==("casado"):
    print("APROBADO")
elif edad==45:
    print ("APROBADO")
elif edad==55: 
    print("APROBADO")
elif ing>2500000:
    print("APROBADO")
elif ing>3500000:
    print("APROBADO")
elif prs>5:
    print("APROBADO")
elif dnv==("campo"):
    print("APROBADO")
elif nmr<2:
    print("APROBADO")
elif est==("SOLTERO"):
    print("APROBADO")
elif dnv==("ciudad"):
    print("APROBADO")