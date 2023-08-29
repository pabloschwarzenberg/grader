ingreso = eval(input("Ingreso(en pesos): "))
año_nacimiento = eval(input("Año de nacimiento: "))
n_hijos = eval(input("Numero de hijos: "))
p_banco = eval(input("Años de pertenencia al banco"))
e_civil = input("Estado civil: ")
donde_vive = input("Vive en campo o ciudad: ")
if (p_banco >10) and (n_hijos>=2):
    print ("APROBADO")
elif e_civil =="casado" and n_hijos >3 and año_nacimiento>=1966 and año_nacimiento<=1975 :
    print ("APROBADO")
elif ingreso>2500000 and e_civil =="S" and donde_vive =="U":
    print ("APROBADO")
elif ingreso>3500000 and p_banco>5:
    print ("APROBADO")
elif e_civil=="C" and donde_vive =="R" and n_hijos <2:
    print ("APROBADO")
else: print ("RECHAZADO")