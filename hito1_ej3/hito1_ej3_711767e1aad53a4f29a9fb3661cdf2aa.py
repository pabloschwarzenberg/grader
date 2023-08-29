#Aprobación de créditos
#introduccion
print("Para saber si le podemos dar un credito necesitamos que nos de algunos datos")
ingreso=int(input("Cuanto dinero gana mensualmente?: "))
nacimiento=int(input("Cuantos años tiene?: "))
hijos=int(input("Cuantos hijos tiene?: "))
pb=int(input("Hace cuanto tiempo pertenece al banco?: "))
civil=(input("Es usted soltero o casado (marque con S o C): "))
cc=(input("Vive en Ciudad o Campo? (Marque con U de urbano o con R de rural): "))
#Desarrollo
if pb > 10 and hijos >= 2:
    print("APROBADO")
elif civil.upper() == "C" and hijos>3 and nacimiento > 45 and nacimiento < 55:
    print("APROBADO")
elif ingreso > 2500000 and civil.upper() == "S" and cc.upper() == "U":
    print("APROBADO")
elif ingreso > 3500000 and pb > 5:
    print("APROBADO")
elif cc.upper() == "R" and civil.upper() == "C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")