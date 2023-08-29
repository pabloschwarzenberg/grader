#Aprobación de créditos

x = int(input("Ingreso monetario:"))
edad = int(input("año de nacimiento:"))
n = int(input("Cuantos Hijos tiene:"))
p = int(input("años de presencia en el banco:"))
v = str(input("Estado Civil:"))
s = str(input("Donde vive!:"))

edad = 2021 - edad

if p>=10:
    print("APROBADO")
elif n>=2:
    print("APROBADO")
elif v==("casado"):
    print("APROBADO") 
elif edad==45:
    print ("APROVADO")
elif edad==55: 
    print("APROVADO")
elif x>2500000:
    print("APROBADO")
elif x>3500000:
    print("APROVADO")
elif p>5:
    print("APROVADO")
elif s==("campo"):
    print("APROBADO")
elif n<2:
    print("APROVADO")
elif v==("SOLTERO"):
    print("aprovado")
elif s==("ciudad"):
    print("APROBADO")
    