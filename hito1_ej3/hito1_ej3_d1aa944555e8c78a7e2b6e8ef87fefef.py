#Aprobación de créditos
ingreso=int(input("Ingrese su ingreso en pesos: "))
nacimiento=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese su numero de hijos: "))
añosbanco=int(input("Ingrese sus años de pertenencia al banco: "))
estadocivil=input("Ingrese su estado civil (S: soltero, C, casado): ")
campociudad=input("ingrese su entorno (U: urbano, R: rural): ")
edad = 2021-nacimiento

if añosbanco > 10 and hijos >= 2:
    print("APROBADO")
elif estadocivil == "C" or estadocivil == "c" and hijos >3 and 45<=edad<=55:
    print("APROBADO")
elif ingreso>2500000 and estadocivil == "S" or estadocivil=="s" and campociudad == "U" or campociudad == "u":
    print("APROBADO")
elif ingreso >3500000 and añosbanco > 5:
    print("APROBADO")
elif campociudad == "C" or campociudad == "c" and estadocivil == "C" or estadocivil == "c" and hijos <2:
    print("APROBADO")

else:
    print("RECHAZADO")
      